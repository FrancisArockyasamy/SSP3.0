from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.ApplicantDetailCreate)
def create_applicant_detail(detail: schemas.ApplicantDetailCreate, db: Session = Depends(database.get_db)):
    db_detail = crud.create_applicant_detail(db, detail)
    return db_detail
