from fastapi import APIRouter,Depends
import schemas
from sqlalchemy.orm import Session
import models,database

router = APIRouter()

@router.get("/passengers_by_bus/{bus_number}")
async def get_passengers_by_bus(bus_number: str, db: Session = Depends(database.get_db)):
    passenger_by_bus = db.query(models.Bus).filter(models.Bus.bus_number == bus_number).first()
    return passenger_by_bus