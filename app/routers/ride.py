from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import async_session
from app.models import RideRequest, Cab
from app.schemas import RideRequestCreate, RideRequestResponse
from app.services.pooling import haversine_distance
from app.services.pricing import calculate_fare
from app.services.concurrency import assign_cab_safe
from typing import List

router = APIRouter()

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# -----------------------------
# POST /rides - Create a ride request
# -----------------------------
@router.post("/", response_model=RideRequestResponse)
async def create_ride(ride: RideRequestCreate, session: AsyncSession = Depends(get_session)):
    # Save ride request to DB
    new_ride = RideRequest(
        pickup_lat=ride.pickup_lat,
        pickup_lon=ride.pickup_lon,
        drop_lat=ride.drop_lat,
        drop_lon=ride.drop_lon,
        seats_required=ride.seats_required,
        max_detour_minutes=ride.max_detour_minutes,
        status="pending"
    )
    session.add(new_ride)
    await session.commit()
    await session.refresh(new_ride)
    return new_ride

# -----------------------------
# GET /rides - List all rides
# -----------------------------
@router.get("/", response_model=List[RideRequestResponse])
async def list_rides(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(RideRequest))
    rides = result.scalars().all()
    return rides

# -----------------------------
# POST /rides/pool - Run pooling algorithm
# -----------------------------
@router.post("/pool")
async def pool_rides(session: AsyncSession = Depends(get_session)):
    # Get pending rides and available cabs
    result_rides = await session.execute(select(RideRequest).where(RideRequest.status == "pending"))
    pending_rides = result_rides.scalars().all()

    result_cabs = await session.execute(select(Cab).where(Cab.available_seats > 0))
    available_cabs = result_cabs.scalars().all()

    grouped = []

    for cab in available_cabs:
        for ride in pending_rides:
            if ride.status != "pending":
                continue
            distance = haversine_distance(cab.current_lat, cab.current_lng, ride.pickup_lat, ride.pickup_lon)
            if distance <= 5 and cab.available_seats >= ride.seats_required:  # Max detour km = 5
                # Concurrency-safe seat assignment
                success = await assign_cab_safe(session, cab.id, ride.seats_required)
                if success:
                    ride.cab_id = cab.id
                    ride.status = "assigned"
                    fare = calculate_fare(base_rate=50, distance_km=distance, rate_per_km=10,
                                          passengers_in_cab=(cab.total_seats - cab.available_seats + ride.seats_required),
                                          demand_factor=1.0)
                    ride.fare = fare
                    session.add(ride)
                    grouped.append({"ride_id": ride.id, "cab_id": cab.id, "fare": fare})

    await session.commit()
    return {"grouped_rides": grouped}

# -----------------------------
# POST /rides/{ride_id}/cancel
# -----------------------------
@router.post("/{ride_id}/cancel")
async def cancel_ride(ride_id: int, session: AsyncSession = Depends(get_session)):

    # Lock ride row
    result = await session.execute(
        select(RideRequest)
        .where(RideRequest.id == ride_id)
        .with_for_update()
    )
    ride = result.scalar_one_or_none()

    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")

    if ride.status == "cancelled":
        raise HTTPException(status_code=400, detail="Ride already cancelled")

    if ride.status == "assigned" and ride.cab_id:
        # Lock cab row safely
        result_cab = await session.execute(
            select(Cab)
            .where(Cab.id == ride.cab_id)
            .with_for_update()
        )
        cab = result_cab.scalar_one()

        # Rollback seats
        cab.available_seats += ride.seats_required

        session.add(cab)

    ride.status = "cancelled"
    session.add(ride)

    await session.commit()

    return {"message": "Ride cancelled successfully"}
