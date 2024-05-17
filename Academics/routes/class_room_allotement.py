from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from models import Class , Room , ClassScheduleAllocation
from db import get_db
import schemas
from datetime import datetime


app = APIRouter(tags=["Class Room Allotment"])

# Dependency to check if a class exists
async def class_exists(class_id: int, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj

# Dependency to check if a room exists
async def room_exists(room_id: int, db: Session = Depends(get_db)):
    room_obj = db.query(Room).filter(Room.id == room_id).first()
    if not room_obj:
        raise HTTPException(status_code=404, detail="Room not found")
    return room_obj



# 1. GET /class_schedule_allocations (Optional filters):
@app.get("/class_schedule_allocations")
async def get_all_class_schedule_allocations(
    class_id: int | None = None,room_id: int | None = None, date: str | None = None, db: Session = Depends(get_db)
):
    # Implement filtering logic based on provided parameters
    allocations = db.query(ClassScheduleAllocation)
    if class_id:
        allocations = allocations.filter(ClassScheduleAllocation.class_id == class_id)
    if room_id:
        allocations = allocations.filter(ClassScheduleAllocation.room_id == room_id)
    if date:
        allocations = allocations.filter(ClassScheduleAllocation.date == date)
    result = allocations.all()

    return result


# 2. POST /class_schedule_allocations: Create a new allocation
@app.post("/class_schedule_allocations")
async def create_class_schedule_allocation(data: schemas.ClassScheduleAllocation, db: Session = Depends(get_db)):
    await class_exists(data.class_id, db)
    await room_exists(data.room_id, db)

    # Check for existing allocation conflicts for classes
    existing_class_allocations = db.query(ClassScheduleAllocation).filter(
        ClassScheduleAllocation.class_id == data.class_id,
        ClassScheduleAllocation.date == datetime.strptime(data.date, "%Y-%m-%d").date(),
        ClassScheduleAllocation.period == data.period,
    ).first()

    if existing_class_allocations:
        raise HTTPException(
            status_code=409, detail="Class already has an allocation for this date and period"
        )
    
    # Check for existing allocation conflicts for rooms
    existing_room_allocations = db.query(ClassScheduleAllocation).filter(
        ClassScheduleAllocation.room_id == data.room_id,
        ClassScheduleAllocation.date == datetime.strptime(data.date, "%Y-%m-%d").date(),
        ClassScheduleAllocation.period == data.period,
    ).first()

    
    if existing_room_allocations:
        raise HTTPException(
            status_code=409, detail=f"Room has been already allocated to another class for this date and period"
        )
    
    if data.period>8:
        raise HTTPException(
            status_code=409, detail="A day has only 8 Periods"
        )

    new_allocation = ClassScheduleAllocation(**data.model_dump())
    db.add(new_allocation)
    db.commit()
    db.refresh(new_allocation)
    return new_allocation




# 5. DELETE /class_schedule_allocations/{allocation_id}: Delete a class-room allocation
@app.delete("/class_schedule_allocations/{allocation_id}")
async def delete_class_schedule_allocation(
    date: str,period: int, class_id: int | None = None, room_id: int | None = None ,db: Session = Depends(get_db)
):
    tempDate = datetime.strptime(date, "%Y-%m-%d").date()
    

    allocations = db.query(ClassScheduleAllocation).filter(ClassScheduleAllocation.date==tempDate,ClassScheduleAllocation.period==period)
    if class_id is None and room_id is None:
        raise HTTPException(
            status_code=422, detail=f"Enter either Class id or Room id to proceed"
        )

    if class_id:
        allocations = allocations.filter(ClassScheduleAllocation.class_id == class_id)
    if room_id:
        allocations = allocations.filter(ClassScheduleAllocation.room_id == room_id)
    result = allocations.first()


    tempRoomClass = "Class" if class_id else "Room"
   
    if not result:
        raise HTTPException(status_code=404, detail=f"{tempRoomClass} allocation not found")

    db.delete(result)
    db.commit()
    return {"message": "Class allocation deleted successfully"}