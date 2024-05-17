from fastapi import APIRouter , Depends , HTTPException
from db import get_db
from  models import Room
from sqlalchemy.orm import Session
import schemas

app = APIRouter(tags=["Rooms"])

@app.get("/rooms")
async def get_all_rooms(db: Session = Depends(get_db)):
    rooms = db.query(Room).all()
    return rooms


@app.post("/rooms")
async def create_room(room_data: schemas.Room, db: Session = Depends(get_db)):
    new_room = Room(**room_data.model_dump())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room


@app.get("/rooms/{room_id}")
async def get_room_by_id(room_id: int, db: Session = Depends(get_db)):
    room_obj = db.query(Room).filter(Room.id == room_id).first()
    if not room_obj:
        raise HTTPException(status_code=404, detail="Room not found")
    return room_obj


@app.put("/rooms/{room_id}")
async def update_room(room_id: int, room_data: schemas.Room, db: Session = Depends(get_db)):
    room_obj = db.query(Room).filter(Room.id == room_id).first()
    if not room_obj:
        raise HTTPException(status_code=404, detail="Room not found")
    for field, value in room_data.model_dump().items():
        setattr(room_obj, field, value)
    db.commit()
    db.refresh(room_obj)
    return room_obj



@app.delete("/rooms/{room_id}")
async def delete_room(room_id: int, db: Session = Depends(get_db)):
    room_obj = db.query(Room).filter(Room.id == room_id).first()
    if not room_obj:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(room_obj)
    db.commit()
    return {"message": "Room deleted successfully"}