from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Attendance
from . import schema

router = APIRouter()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example endpoint to create an attendance record
@router.post("/attendance/", response_model=schema.Attendance)
def create_attendance_record(attendance: schema.Attendance, db: Session = Depends(get_db)):
    db_data = Attendance(**attendance.dict())  # Assuming models.Attendance is properly defined
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

# Example endpoint to get a specific attendance record by ID
@router.get("/attendance/{attendance_id}", response_model=schema.Attendance)
def read_attendance_record(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance

# Example endpoint to update an attendance record
@router.put("/attendance/{attendance_id}", response_model=schema.Attendance)
def update_attendance_record(attendance_id: int, attendance: schema.Attendance, db: Session = Depends(get_db)):
    db_attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not db_attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    for key, value in attendance.dict().items():
        setattr(db_attendance, key, value)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# Example endpoint to delete an attendance record
@router.delete("/attendance/{attendance_id}")
def delete_attendance_record(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    db.delete(attendance)
    db.commit()
    return {"message": "Attendance record deleted"}
