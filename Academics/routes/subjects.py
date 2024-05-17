from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from models import Subject
from db import get_db
import schemas

app=APIRouter(tags=["Subjects"])



@app.get("/subjects")
async def get_all_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return subjects


@app.post("/subjects")
async def create_subject(subject_data: schemas.Subject, db: Session = Depends(get_db)):
    new_subject = Subject(**subject_data.model_dump())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject


@app.get("/subjects/{subject_id}")
async def get_subject_by_id(subject_id: int, db: Session = Depends(get_db)):
    subject_obj = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject_obj:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject_obj


@app.put("/subjects/{subject_id}")
async def update_subject(subject_id: int, subject_data: schemas.Subject, db: Session = Depends(get_db)):
    subject_obj = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject_obj:
        raise HTTPException(status_code=404, detail="Subject not found")
    for field, value in subject_data.model_dump().items():
        setattr(subject_obj, field, value)
    db.commit()
    db.refresh(subject_obj)
    return subject_obj



@app.delete("/subjects/{subject_id}")
async def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    subject_obj = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject_obj:
        raise HTTPException(status_code=404, detail="Subject not found")
    db.delete(subject_obj)
    db.commit()
    return {"message": "Subject deleted successfully"}