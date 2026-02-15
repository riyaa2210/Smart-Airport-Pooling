from fastapi import FastAPI, Depends
from app.database import async_session
from app.models import Base, RideRequest
from app.routers import ride, cab
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text
import time

app = FastAPI()


# Middleware for process time
@app.middleware("http")
async def add_process_time(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response


# Async session dependency
async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


# Root path (only ONE root)
@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"message": "Smart Airport API Running 🚀"}


# Example: list all rides
@app.get("/rides")
async def list_rides(session: AsyncSession = Depends(get_db)):
    result = await session.execute(select(RideRequest))
    rides = result.scalars().all()
    return rides


# Include routers
app.include_router(ride.router, prefix="/rides", tags=["rides"])
app.include_router(cab.router, prefix="/cabs", tags=["cabs"])
