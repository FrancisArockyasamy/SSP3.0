from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.AdmissionFormCreate)
def create_admission_form(form: schemas.AdmissionFormCreate, db: Session = Depends(database.get_db)):
    db_form = crud.create_admission_form(db, form)
    return db_form
