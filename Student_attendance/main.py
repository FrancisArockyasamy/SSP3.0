from fastapi import FastAPI, HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from .models import Base, Student, Attendance
from .database import SessionLocal, engine
from datetime import date

app = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create
@app.post("/students/")
def create_student(student_name: str, db: Session = Depends(get_db)):
    new_student = Student(student_name=student_name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# Read
@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update
@app.put("/students/{student_id}")
def update_student(student_id: int, student_name: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student.student_name = student_name
    db.commit()
    return {"message": "Student updated successfully"}

# Delete
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

# Create attendance record
@app.post("/attendance/")
def create_attendance(student_id: int, attendance_date: date, attendance_status: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    new_attendance = Attendance(student_id=student_id, attendance_date=attendance_date, attendance_status=attendance_status)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

# Read attendance record
@app.get("/attendance/{attendance_id}")
def read_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if attendance is None:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance

# Update attendance record
@app.put("/attendance/{attendance_id}")
def update_attendance(attendance_id: int, attendance_status: str, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if attendance is None:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    attendance.attendance_status = attendance_status
    db.commit()
    return {"message": "Attendance record updated successfully"}

# Delete attendance record
@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if attendance is None:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    db.delete(attendance)
    db.commit()
    return {"message": "Attendance record deleted successfully"}
