from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter()

@router.post("/passengers/", response_model=schemas.Passenger)
async def create_passenger(passenger: schemas.PassengerCreate, db: Session = Depends(database.get_db)):
    db_passenger = models.Passenger(**passenger.dict())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

@router.get("/passengers/", response_model=List[schemas.Passenger])
async def read_passengers(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    passengers = db.query(models.Passenger).offset(skip).limit(limit).all()
    return passengers

@router.get("/passengers/{passenger_id}", response_model=schemas.Passenger)
async def read_passenger(passenger_id: int, db: Session = Depends(database.get_db)):
    passenger = db.query(models.Passenger).filter(models.Passenger.passenger_id == passenger_id).first()
    if passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger
