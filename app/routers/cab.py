from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Cab
from app.schemas import CabCreate
from app.dependencies import get_db

router = APIRouter(prefix="/cab", tags=["Cab"])


@router.post("/")
def add_cab(cab: CabCreate, db: Session = Depends(get_db)):
    new_cab = Cab(
        driver_name=cab.driver_name,
        total_seats=cab.total_seats,
        available_seats=cab.total_seats,
        max_luggage=cab.max_luggage,
        available_luggage=cab.max_luggage,
        current_lat=cab.current_lat,
        current_lng=cab.current_lng
    )
    db.add(new_cab)
    db.commit()
    db.refresh(new_cab)
    return new_cab
