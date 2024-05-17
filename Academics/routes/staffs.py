from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from ..models import Staff
from .. import schemas
from ..db import get_db

app=APIRouter(tags=["Staffs"])


@app.get("/staff")
async def get_all_staff(db: Session = Depends(get_db)):
    staff_list = db.query(Staff).all()
    return staff_list


@app.post("/staff")
async def create_staff(staff_data: schemas.Staff, db: Session = Depends(get_db)):
    new_staff = Staff(**staff_data.model_dump())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff


@app.get("/staff/{staff_id}")
async def get_staff_by_id(staff_id: int, db: Session = Depends(get_db)):
    staff_obj = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff_obj:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return staff_obj


@app.put("/staff/{staff_id}")
async def update_staff(staff_id: int, staff_data: schemas.Staff, db: Session = Depends(get_db)):
    staff_obj = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff_obj:
        raise HTTPException(status_code=404, detail="Staff member not found")
    for field, value in staff_data.model_dump().items():
        setattr(staff_obj, field, value)
    db.commit()
    db.refresh(staff_obj)
    return staff_obj



@app.delete("/staff/{staff_id}")
async def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    staff_obj = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff_obj:
        raise HTTPException(status_code=404, detail="Staff member not found")
    db.delete(staff_obj)
    db.commit()
    return {"message": "Staff member deleted successfully"}