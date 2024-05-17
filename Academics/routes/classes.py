from fastapi import FastAPI, Depends, HTTPException , APIRouter
from sqlalchemy.orm import Session
from ..db import get_db

from ..models import Class  # Assuming models.py is in the same directory
from .. import schemas  # Assuming schemas.py is in the same directory

app = APIRouter(tags=["Classes"])

@app.post("/classes")
async def create_class(class_data: schemas.Class, db: Session = Depends(get_db)):
    new_class = Class(**class_data.model_dump())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@app.get("/classes")
async def get_class_by_id(db: Session = Depends(get_db)):
    class_obj = db.query(Class).all()
    return class_obj


@app.get("/classes/{class_id}")
async def get_class_by_id(class_id: int, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj



@app.put("/classes/{class_id}")
async def update_class(class_id: int, class_data: schemas.Class, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    for field, value in class_data.model_dump().items():
        setattr(class_obj, field, value)
    db.commit()
    db.refresh(class_obj)
    return class_obj


@app.delete("/classes/{class_id}")
async def delete_class(class_id: int, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(class_obj)
    db.commit()
    return {"message": "Class deleted successfully"}