from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models import PassengerByBus
from .. import schemas
from ..database import get_db

router = APIRouter()

# Create a new passenger by bus record
@router.post("/passengers_by_bus/", response_model=schemas.PassengerByBus)
def create_passenger_by_bus(passenger_by_bus: schemas.PassengerByBusCreate, db: Session = Depends(get_db)):
    new_passenger_by_bus = PassengerByBus(**passenger_by_bus.dict())
    db.add(new_passenger_by_bus)
    db.commit()
    db.refresh(new_passenger_by_bus)
    return new_passenger_by_bus

# Get a list of all passengers by bus records
@router.get("/passengers_by_bus/", response_model=List[schemas.PassengerByBus])
def read_passengers_by_bus(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    passengers_by_bus = db.query(PassengerByBus).offset(skip).limit(limit).all()
    return passengers_by_bus

# Get a single passenger by bus record by ID
@router.get("/passengers_by_bus/{passenger_by_bus_id}", response_model=schemas.PassengerByBus)
def read_passenger_by_bus(passenger_by_bus_id: int, db: Session = Depends(get_db)):
    db_passenger_by_bus = db.query(PassengerByBus).filter(PassengerByBus.id == passenger_by_bus_id).first()
    if db_passenger_by_bus is None:
        raise HTTPException(status_code=404, detail="Passenger by bus not found")
    return db_passenger_by_bus

# Update a passenger by bus record by ID
@router.put("/passengers_by_bus/{passenger_by_bus_id}", response_model=schemas.PassengerByBus)
def update_passenger_by_bus(passenger_by_bus_id: int, passenger_by_bus: schemas.PassengerByBusUpdate, db: Session = Depends(get_db)):
    db_passenger_by_bus = db.query(PassengerByBus).filter(PassengerByBus.id == passenger_by_bus_id).first()
    if db_passenger_by_bus is None:
        raise HTTPException(status_code=404, detail="Passenger by bus not found")
    for key, value in passenger_by_bus.dict().items():
        setattr(db_passenger_by_bus, key, value)
    db.commit()
    db.refresh(db_passenger_by_bus)
    return db_passenger_by_bus

# Delete a passenger by bus record by ID
@router.delete("/passengers_by_bus/{passenger_by_bus_id}", response_model=schemas.PassengerByBus)
def delete_passenger_by_bus(passenger_by_bus_id: int, db: Session = Depends(get_db)):
    db_passenger_by_bus = db.query(PassengerByBus).filter(PassengerByBus.id == passenger_by_bus_id).first()
    if db_passenger_by_bus is None:
        raise HTTPException(status_code=404, detail="Passenger by bus not found")
    db.delete(db_passenger_by_bus)
    db.commit()
    return db_passenger_by_bus
