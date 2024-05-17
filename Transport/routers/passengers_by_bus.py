from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import models,database,schemas

router = APIRouter()

@router.get("/passengers_by_bus/{bus_number}")
async def get_passengers_by_bus(bus_number: str, db: Session = Depends(database.get_db)):
    passenger_by_bus = db.query(models.Bus).filter(models.Bus.bus_number == bus_number).first()
    return passenger_by_bus

# @router.put("/passengers_by_bus/{trip_number}/{bus_number}", response_model=schemas.PassengerByBus)
# async def update_passengers_by_bus(trip_number: str, bus_number: str, passengers: schemas.PassengerByBus, db: Session = Depends(database.get_db)):
#     bus = db.query(models.Bus).filter(models.Bus.trip_number == trip_number, models.Bus.bus_number == bus_number).first()
#     if not bus:
#         raise HTTPException(status_code=404, detail="Bus not found")

#     bus.passengers = passengers.passengers  # Assuming `passengers` is a column in your `Bus` model
#     db.commit()
#     db.refresh(bus)
#     return passengers

# @router.delete("/passengers_by_bus/{trip_number}/{bus_number}")
# async def delete_passengers_by_bus(trip_number: str, bus_number: str, db: Session = Depends(database.get_db)):
#     bus = db.query(models.Bus).filter(models.Bus.trip_number == trip_number, models.Bus.bus_number == bus_number).first()
#     if not bus:
#         raise HTTPException(status_code=404, detail="Bus not found")

#     db.delete(bus)
#     db.commit()
#     return {"message": "Deleted successfully"}