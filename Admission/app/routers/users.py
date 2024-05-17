from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models, database

router = APIRouter()

@router.post("/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.create_user(db, user)
    return db_user
