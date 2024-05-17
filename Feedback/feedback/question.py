from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model, schemas, database

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/", response_model=schemas.Question)
async def create_question(question: schemas.QuestionCreate, db: Session = Depends(database.get_db)):
    db_question = model.Question(
        form_id=question.form_id, question_text=question.question_text, question_type=question.question_type
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
