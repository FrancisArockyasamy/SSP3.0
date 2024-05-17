from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schema, database
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shifts/", response_model=schema.ShiftResponse)
def create_shift(shift: schema.ShiftCreate, db: Session = Depends(get_db)):
    db_shift = models.Shift(**shift.dict())
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    
    return {
        "ShiftID": db_shift.ShiftID,
        "ShiftName": db_shift.ShiftName,
        "StartTime": db_shift.StartTime,
        "EndTime": db_shift.EndTime
    }

# @app.post("/shifts/", response_model=schema.ShiftResponse)
# def create_shift(shift: schema.ShiftCreate, db: Session = Depends(get_db)):
#     db_shift = models.Shift(**shift.dict())
#     db.add(db_shift)
#     db.commit()
#     db.refresh(db_shift)
#     return db_shift

@app.post("/subjects/", response_model=schema.SubjectBase)
def create_subject(subject: schema.SubjectCreate, db: Session = Depends(get_db)):
    db_subject = models.Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

@app.post("/teachers/", response_model=schema.TeacherBase)
def create_teacher(teacher: schema.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@app.post("/classes/", response_model=schema.ClassBase)
def create_class(class_: schema.ClassCreate, db: Session = Depends(get_db)):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

@app.post("/timetables/", response_model=schema.TimetableBase)
def create_timetable(timetable: schema.TimetableCreate, db: Session = Depends(get_db)):
    db_timetable = models.Timetable(**timetable.dict())
    db.add(db_timetable)
    db.commit()
    db.refresh(db_timetable)
    return db_timetable


Base.metadata.create_all(bind= engine)