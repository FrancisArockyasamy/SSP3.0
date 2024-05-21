from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from .schemas import HomeworkAssignmentCreate, GradeCreate, HomeworkSubmission,TeacherCreate,StudentCreate,Teacher,Student,Subject,SubjectCreate,HomeworkAssignment,HomeworkSubmissionCreate,Grade
from typing import List
app = APIRouter(
     prefix="/homework",
    tags=["Homework"]
)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/homework/assign", response_model=HomeworkAssignment)
def create_homework_assignment(assignment:HomeworkAssignmentCreate, db: Session = Depends(get_db)):
    db_assignment = models.HomeworkAssignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

# List students
@app.get("/homework/assign_list_withoutlimit", response_model=List[HomeworkAssignment])
def teacher_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(models.HomeworkAssignment).all()

@app.post("/submission", response_model=HomeworkSubmission)
def create_homework_submission(submission: HomeworkSubmissionCreate, db: Session = Depends(get_db)):
    db_submission = models.HomeworkSubmission(**submission.dict())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

# List students
@app.get("/homework/submission_list_withoutlimit", response_model=List[HomeworkSubmission])
def teacher_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(models.HomeworkSubmission).all()

@app.post("/grade",response_model=Grade)
def create_grade(grade: GradeCreate,db: Session = Depends(get_db)):
    db_grade = models.Grade(**grade.dict())
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

@app.post("/teachers", response_model=Teacher)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    db_teacher =models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# List students
@app.get("/teacher_list_withoutlimit/", response_model=List[Teacher])
def teacher_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()

@app.post("/students", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# List students
@app.get("/students_list_withoutlimit/", response_model=List[Student])
def students_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@app.post("/subjects/", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    db_subject = models.Subject(**subject.dict())  
    db.add(db_subject)  
    db.commit() 
    db.refresh(db_subject)
    return db_subject

# List students
@app.get("/subject_list_withoutlimit/", response_model=List[Subject])
def subject_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(models.Subject).all()