from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.FormFieldCreate)
def create_form_field(field: schemas.FormFieldCreate, db: Session = Depends(database.get_db)):
    db_field = crud.create_form_field(db, field)
    return db_field
