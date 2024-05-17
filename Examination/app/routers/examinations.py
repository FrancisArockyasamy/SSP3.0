from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, models, database

router = APIRouter(
    prefix="/examinations",
    tags=["examinations"],
)

@router.post("/")
def create_examination(exam: schemas.ExaminationCreate, db: Session = Depends(database.get_db)):
    db_exam = models.Examination(**exam.model_dump())
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

# Define other endpoints similarly

@router.get("/", response_model=list[schemas.Examination])
def read_examinations(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    exams = crud.get_examinations(db, skip=skip, limit=limit)
    return exams

@router.get("/{exam_id}", response_model=schemas.Examination)
def read_examination(exam_id: int, db: Session = Depends(database.get_db)):
    exam = crud.get_examination(db, exam_id=exam_id)
    if exam is None:
        raise HTTPException(status_code=404, detail="Examination not found")
    return exam

@router.put("/{exam_id}", response_model=schemas.Examination)
def update_examination(exam_id: int, exam: schemas.ExaminationUpdate, db: Session = Depends(database.get_db)):
    db_exam = crud.get_examination(db, exam_id=exam_id)
    if db_exam is None:
        raise HTTPException(status_code=404, detail="Examination not found")
    return crud.update_examination(db=db, exam_id=exam_id, exam=exam)

@router.delete("/{exam_id}", response_model=schemas.Examination)
def delete_examination(exam_id: int, db: Session = Depends(database.get_db)):
    db_exam = crud.get_examination(db, exam_id=exam_id)
    if db_exam is None:
        raise HTTPException(status_code=404, detail="Examination not found")
    return crud.delete_examination(db=db, exam_id=exam_id)

