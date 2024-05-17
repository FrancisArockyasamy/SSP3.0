from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from .schemas import HomeworkAssignmentCreate, GradeCreate, HomeworkSubmission  # Import the required classes from schemas

app = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post("/assign")
# def create_homework_assignment(assignment: HomeworkAssignmentCreate, db: Session = Depends(get_db)):
#     return crud.create_homework_assignment(db, assignment)



@app.post("/assign")
def create_homework_assignment( assignment: HomeworkAssignmentCreate,db: Session = Depends(get_db)):
    db_assignment = models.HomeworkAssignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@app.post("/submission")
def create_homework_submission( submission: HomeworkSubmission,db: Session = Depends(get_db)):
    db_submission = models.HomeworkSubmission(**submission.dict())
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

@app.post("/grade")
def create_grade(grade: GradeCreate,db: Session = Depends(get_db)):
    db_grade = models.Grade(**grade.dict())
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade
