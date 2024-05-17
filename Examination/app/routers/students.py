from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, models, database

router = APIRouter(
    prefix="/students",
    tags=["students"],
)

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@router.delete("/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_student(db=db, student_id=student_id)