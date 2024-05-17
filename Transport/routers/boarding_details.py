from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter()

@router.post("/boarding_details/", response_model=schemas.BoardingDetail)
async def create_boarding_detail(boarding_detail: schemas.BoardingDetailCreate, db: Session = Depends(database.get_db)):
    db_boarding_detail = models.BoardingDetail(**boarding_detail.dict())
    db.add(db_boarding_detail)
    db.commit()
    db.refresh(db_boarding_detail)
    return db_boarding_detail

@router.get("/boarding_details/", response_model=List[schemas.BoardingDetail])
async def read_boarding_details(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    boarding_details = db.query(models.BoardingDetail).offset(skip).limit(limit).all()
    return boarding_details

@router.get("/boarding_details/{boarding_id}", response_model=schemas.BoardingDetail)
async def read_boarding_detail(boarding_id: int, db: Session = Depends(database.get_db)):
    boarding_detail = db.query(models.BoardingDetail).filter(models.BoardingDetail.boarding_id == boarding_id).first()
    if boarding_detail is None:
        raise HTTPException(status_code=404, detail="Boarding detail not found")
    return boarding_detail
