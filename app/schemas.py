from pydantic import BaseModel, Field, conint, confloat
from typing import Optional


# -------------------------------
# Passenger Models
# -------------------------------
class PassengerCreate(BaseModel):
    name: str
    phone: str

class PassengerResponse(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True


# -------------------------------
# Cab Models
# -------------------------------
class CabCreate(BaseModel):
    driver_name: str
    total_seats: conint(gt=0)
    max_luggage: conint(ge=0)
    current_lat: confloat(ge=-90, le=90)
    current_lng: confloat(ge=-180, le=180)

class CabResponse(BaseModel):
    id: int
    driver_name: str
    total_seats: int
    available_seats: int
    max_luggage: int
    current_lat: float
    current_lng: float

    model_config = {
    "from_attributes": True
}



# -------------------------------
# Ride Request Models
# -------------------------------
class RideRequestCreate(BaseModel):
    pickup_lat: confloat(ge=-90, le=90)
    pickup_lon: confloat(ge=-180, le=180)
    drop_lat: confloat(ge=-90, le=90)
    drop_lon: confloat(ge=-180, le=180)
    seats_required: conint(gt=0)
    max_detour_minutes: conint(gt=0) = 10

class RideRequestResponse(BaseModel):
    id: int
    passenger_id: int
    cab_id: Optional[int] = None
    pickup_lat: float
    pickup_lon: float
    drop_lat: float
    drop_lon: float
    seats_required: int
    max_detour_minutes: int
    status: str  # pending / assigned / cancelled

    model_config = {
    "from_attributes": True
}

