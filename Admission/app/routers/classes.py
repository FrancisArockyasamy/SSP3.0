from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.ClassCreate)
def create_class(cls: schemas.ClassCreate, db: Session = Depends(database.get_db)):
    db_class = crud.create_class(db, cls)
    return db_class
