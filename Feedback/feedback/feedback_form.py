from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import model, schemas, database

router = APIRouter(prefix="/feedback_forms", tags=["Feedback Forms"])

@router.post("/", response_model=schemas.FeedbackForm)
async def create_feedback_form(form: schemas.FeedbackFormCreate, db: Session = Depends(database.get_db)):
    db_form = model.FeedbackForm(title=form.title, description=form.description, created_by=1)  # Replace with actual user_id
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form
