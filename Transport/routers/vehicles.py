from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter()

@router.post("/vehicles/", response_model=schemas.Vehicle)
async def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(database.get_db)):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.get("/vehicles/", response_model=List[schemas.Vehicle])
async def read_vehicles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    vehicles = db.query(models.Vehicle).offset(skip).limit(limit).all()
    return vehicles

@router.get("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
async def read_vehicle(vehicle_id: int, db: Session = Depends(database.get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vehicle_id == vehicle_id).first()
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle
