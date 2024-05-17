from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, database

router = APIRouter()

@router.post("/buses/", response_model=schemas.Bus)
async def create_bus(bus: schemas.BusCreate, db: Session = Depends(database.get_db)):
    db_bus = models.Bus(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

@router.get("/buses/", response_model=List[schemas.Bus])
async def get_buses(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    buses = db.query(models.Bus).offset(skip).limit(limit).all()
    return buses

@router.put("/buses/{bus_id}", response_model=schemas.Bus)
async def update_bus(bus_id: int, bus: schemas.BusCreate, db: Session = Depends(database.get_db)):
    db_bus = db.query(models.Bus).filter(models.Bus.id == bus_id).first()
    if db_bus is None:
        raise HTTPException(status_code=404, detail="Bus not found")
    for key, value in bus.dict().items():
        setattr(db_bus, key, value)
    db.commit()
    db.refresh(db_bus)
    return db_bus

@router.delete("/buses/{bus_id}", response_model=schemas.Bus)
async def delete_bus(bus_id: int, db: Session = Depends(database.get_db)):
    db_bus = db.query(models.Bus).filter(models.Bus.id == bus_id).first()
    if db_bus is None:
        raise HTTPException(status_code=404, detail="Bus not found")
    db.delete(db_bus)
    db.commit()
    return db_bus
