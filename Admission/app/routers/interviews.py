from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.InterviewCreate)
def create_interview(interview: schemas.InterviewCreate, db: Session = Depends(database.get_db)):
    db_interview = crud.create_interview(db, interview)
    return db_interview
