from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.ApplicantCreate)
def create_applicant(applicant: schemas.ApplicantCreate, db: Session = Depends(database.get_db)):
    db_applicant = crud.create_applicant(db, applicant)
    return db_applicant
