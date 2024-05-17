from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime
from typing import List

# Create student
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Get all students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

# Get grades by student ID
def get_grades_by_student_id(db: Session, student_id: int):
    return db.query(models.Grade).filter(models.Grade.student_id == student_id).all()

# Get attendance by student ID
def get_attendance_by_student_id(db: Session, student_id: int):
    return db.query(models.Attendance).filter(models.Attendance.student_id == student_id).all()

# Get student by ID
def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

# Get homework by student ID
def get_homework_by_student_id(db: Session, student_id: int):
    return db.query(models.Homework).filter(models.Homework.student_id == student_id).all()

# Get remarks by student ID
def get_remarks_by_student_id(db: Session, student_id: int):
    return db.query(models.Remark).filter(models.Remark.student_id == student_id).all()

# Get SMS usage by student ID
def get_sms_usage_by_student_id(db: Session, student_id: int):
    return db.query(models.SMSUsage).filter(models.SMSUsage.student_id == student_id).first()

# Get progress cards by student ID
def get_progress_cards_by_student_id(db: Session, student_id: int):
    return db.query(models.ProgressCard).filter(models.ProgressCard.student_id == student_id).all()

# Pay fee
def pay_fee(db: Session, student_id: int, payment: schemas.FeePaymentCreate):
    fee_payment = models.FeePayment(student_id=student_id, payment_date=datetime.now(), **payment.dict())
    db.add(fee_payment)
    db.commit()
    db.refresh(fee_payment)
    return fee_payment

# Get fee payments by student ID
def get_fee_payments_by_student_id(db: Session, student_id: int):
    return db.query(models.FeePayment).filter(models.FeePayment.student_id == student_id).all()

# Create class
def create_class(db: Session, class_: schemas.ClassCreate):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

# Get all classes
def get_classes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Class).offset(skip).limit(limit).all()

# Create teacher
def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# Get all teachers
def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Teacher).offset(skip).limit(limit).all()