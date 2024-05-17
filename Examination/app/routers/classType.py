from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, models, database

router = APIRouter(
    prefix="/class",
    tags=["class"],
)

@router.post("/")
def create_mark(className: schemas.CreateClass, db: Session = Depends(database.get_db)):
    db_mark = models.Class(**className.model_dump())
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark

# Define other endpoints similarly
