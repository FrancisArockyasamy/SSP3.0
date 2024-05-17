from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, models, database

router = APIRouter(
    prefix="/marks",
    tags=["marks"],
)

@router.post("/")
def create_mark(mark: schemas.MarkBase, db: Session = Depends(database.get_db)):
    db_mark = models.Mark(**mark.model_dump())
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark

# Define other endpoints similarly
