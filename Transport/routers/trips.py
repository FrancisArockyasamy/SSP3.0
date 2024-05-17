from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter()

@router.post("/trips/", response_model=schemas.Trip)
async def create_trip(trip: schemas.TripCreate, db: Session = Depends(database.get_db)):
    db_trip = models.Trip(**trip.dict())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

@router.get("/trips/", response_model=List[schemas.Trip])
async def read_trips(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    trips = db.query(models.Trip).offset(skip).limit(limit).all()
    return trips

@router.get("/trips/{trip_id}", response_model=schemas.Trip)
async def read_trip(trip_id: int, db: Session = Depends(database.get_db)):
    trip = db.query(models.Trip).filter(models.Trip.trip_id == trip_id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip
