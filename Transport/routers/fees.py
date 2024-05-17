from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

router = APIRouter()

@router.post("/fees/", response_model=schemas.Fee)
async def create_fee(fee: schemas.FeeCreate, db: Session = Depends(database.get_db)):
    db_fee = models.Fee(**fee.dict())
    db.add(db_fee)
    db.commit()
    db.refresh(db_fee)
    return db_fee

@router.get("/fees/", response_model=List[schemas.Fee])
async def read_fees(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    fees = db.query(models.Fee).offset(skip).limit(limit).all()
    return fees

@router.get("/fees/{fee_id}", response_model=schemas.Fee)
async def read_fee(fee_id: int, db: Session = Depends(database.get_db)):
    fee = db.query(models.Fee).filter(models.Fee.fee_id == fee_id).first()
    if fee is None:
        raise HTTPException(status_code=404, detail="Fee not found")
    return fee
