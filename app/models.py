from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum, Index
from sqlalchemy.orm import relationship
from app.database import Base
import datetime
import enum


class RideStatus(str, enum.Enum):
    PENDING = "PENDING"
    GROUPED = "GROUPED"
    CANCELLED = "CANCELLED"


class CabStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    ON_TRIP = "ON_TRIP"


class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Cab(Base):
    __tablename__ = "cabs"

    id = Column(Integer, primary_key=True, index=True)
    driver_name = Column(String, nullable=False)
    total_seats = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
    max_luggage = Column(Integer, nullable=False)
    available_luggage = Column(Integer, nullable=False)
    current_lat = Column(Float)
    current_lng = Column(Float)
    status = Column(Enum(CabStatus), default=CabStatus.AVAILABLE)

    __table_args__ = (
        Index("idx_cab_status_seats", "status", "available_seats"),
    )


class RideRequest(Base):
    __tablename__ = "ride_requests"

    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey("passengers.id"))
    pickup_lat = Column(Float)
    pickup_lng = Column(Float)
    drop_lat = Column(Float)
    drop_lng = Column(Float)
    seats_required = Column(Integer)
    luggage_units = Column(Integer)
    max_detour_minutes = Column(Integer)
    status = Column(Enum(RideStatus), default=RideStatus.PENDING)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="pending")
    cab_id = Column(Integer, ForeignKey("cabs.id"), nullable=True)
    fare = Column(Float, nullable=True)

    __table_args__ = (
        Index("idx_request_status", "status"),
    )
