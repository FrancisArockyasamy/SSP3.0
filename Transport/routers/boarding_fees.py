from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter()

@router.post("/boarding_fees/", response_model=schemas.BoardingFee)
async def create_boarding_fee(boarding_fee: schemas.BoardingFeeCreate, db: Session = Depends(database.get_db)):
    db_boarding_fee = models.BoardingFee(**boarding_fee.dict())
    db.add(db_boarding_fee)
    db.commit()
    db.refresh(db_boarding_fee)
    return db_boarding_fee

@router.get("/boarding_fees/", response_model=List[schemas.BoardingFee])
async def read_boarding_fees(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    boarding_fees = db.query(models.BoardingFee).offset(skip).limit(limit).all()
    return boarding_fees

@router.get("/boarding_fees/{fee_id}", response_model=schemas.BoardingFee)
async def read_boarding_fee(fee_id: int, db: Session = Depends(database.get_db)):
    boarding_fee = db.query(models.BoardingFee).filter(models.BoardingFee.fee_id == fee_id).first()
    if boarding_fee is None:
        raise HTTPException(status_code=404, detail="Boarding fee not found")
    return boarding_fee

@router.put("/boarding_fees/{fee_id}", response_model=schemas.BoardingFee)
async def update_boarding_fee(fee_id: int, boarding_fee: schemas.BoardingFeeCreate, db: Session = Depends(database.get_db)):
    db_boarding_fee = db.query(models.BoardingFee).filter(models.BoardingFee.fee_id == fee_id).first()
    if db_boarding_fee is None:
        raise HTTPException(status_code=404, detail="Boarding fee not found")
    for key, value in boarding_fee.dict().items():
        setattr(db_boarding_fee, key, value)
    db.commit()
    db.refresh(db_boarding_fee)
    return db_boarding_fee

@router.delete("/boarding_fees/{fee_id}", response_model=schemas.BoardingFee)
async def delete_boarding_fee(fee_id: int, db: Session = Depends(database.get_db)):
    db_boarding_fee = db.query(models.BoardingFee).filter(models.BoardingFee.fee_id == fee_id).first()
    if db_boarding_fee is None:
        raise HTTPException(status_code=404, detail="Boarding fee not found")
    db.delete(db_boarding_fee)
    db.commit()
    return db_boarding_fee