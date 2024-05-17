from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database

router = APIRouter()

@router.post("/buses/", response_model=schemas.Bus)
async def create_bus(bus: schemas.BusCreate, db: Session = Depends(database.get_db)):
    db_bus = models.Bus(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus
