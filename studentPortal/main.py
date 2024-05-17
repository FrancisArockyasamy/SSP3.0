# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create student
@app.post("/students/", response_model=schemas.StudentInDB)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

# Get all students
@app.get("/students/", response_model=List[schemas.StudentInDB])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db=db, skip=skip, limit=limit)
    return students

# View academic performance
@app.get("/students/{student_id}/grades/", response_model=List[schemas.Grade])
def read_grades(student_id: int, db: Session = Depends(get_db)):
    grades = crud.get_grades_by_student_id(db, student_id=student_id)
    if not grades:
        raise HTTPException(status_code=404, detail="Grades not found")
    return grades

# View attendance
@app.get("/students/{student_id}/attendance/", response_model=List[schemas.Attendance])
def read_attendance(student_id: int, db: Session = Depends(get_db)):
    attendance = crud.get_attendance_by_student_id(db, student_id=student_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return attendance

# View profile
@app.get("/students/{student_id}/profile/", response_model=schemas.StudentInDB)
def read_student_profile(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# View homework
@app.get("/students/{student_id}/homework/", response_model=List[schemas.Homework])
def read_homework(student_id: int, db: Session = Depends(get_db)):
    homework = crud.get_homework_by_student_id(db, student_id=student_id)
    if not homework:
        raise HTTPException(status_code=404, detail="Homework not found")
    return homework

# View remarks
@app.get("/students/{student_id}/remarks/", response_model=List[schemas.Remark])
def read_remarks(student_id: int, db: Session = Depends(get_db)):
    remarks = crud.get_remarks_by_student_id(db, student_id=student_id)
    if not remarks:
        raise HTTPException(status_code=404, detail="Remarks not found")
    return remarks

# View SMS usage
@app.get("/students/{student_id}/sms-usage/", response_model=schemas.SMSUsage)
def read_sms_usage(student_id: int, db: Session = Depends(get_db)):
    sms_usage = crud.get_sms_usage_by_student_id(db, student_id=student_id)
    if not sms_usage:
        raise HTTPException(status_code=404, detail="SMS usage not found")
    return sms_usage

# View progress card
@app.get("/students/{student_id}/progress-cards/", response_model=List[schemas.ProgressCard])
def read_progress_cards(student_id: int, db: Session = Depends(get_db)):
    progress_cards = crud.get_progress_cards_by_student_id(db, student_id=student_id)
    if not progress_cards:
        raise HTTPException(status_code=404, detail="Progress cards not found")
    return progress_cards

# Pay fee
@app.post("/students/{student_id}/pay-fee/", response_model=schemas.FeePayment)
def pay_fee(student_id: int, payment: schemas.FeePaymentCreate, db: Session = Depends(get_db)):
    return crud.pay_fee(db=db, student_id=student_id, payment=payment)

# View fee payments
@app.get("/students/{student_id}/fee-payments/", response_model=List[schemas.FeePayment])
def read_fee_payments(student_id: int, db: Session = Depends(get_db)):
    fee_payments = crud.get_fee_payments_by_student_id(db, student_id=student_id)
    if not fee_payments:
        raise HTTPException(status_code=404, detail="Fee payments not found")
    return fee_payments
# Create class
@app.post("/classes/", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db=db, class_=class_)

# Get all classes
@app.get("/classes/", response_model=List[schemas.Class])
def read_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = crud.get_classes(db=db, skip=skip, limit=limit)
    return classes

# Create teacher
@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db=db, teacher=teacher)

# Get all teachers
@app.get("/teachers/", response_model=List[schemas.Teacher])
def read_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teachers = crud.get_teachers(db=db, skip=skip, limit=limit)
    return teachers