from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.AdmissionCreate)
def create_admission(admission: schemas.AdmissionCreate, db: Session = Depends(database.get_db)):
    db_admission = crud.create_admission(db, admission)
    return db_admission
