from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas, models, crud
from database import get_db

router = APIRouter(
    prefix="/feedbacks",
    tags=["feedbacks"],
    responses={404: {"description": "Not found"}},
)

@router.post("/") # , response_model=schemas.Feedback
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db=db, feedback=feedback)

@router.get("/", response_model=List[schemas.Feedback])
def read_feedbacks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    feedbacks = crud.get_feedbacks(db, skip=skip, limit=limit)
    return feedbacks

@router.get("/{feedback_id}", response_model=schemas.Feedback)
def read_feedback(feedback_id: int, db: Session = Depends(get_db)):
    db_feedback = crud.get_feedback(db, feedback_id=feedback_id)
    if db_feedback is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback

@router.post("/{feedback_id}/responses", response_model=schemas.FeedbackResponse)
def create_feedback_response(feedback_id: int, response: schemas.FeedbackResponseCreate, db: Session = Depends(get_db)):
    feedback = crud.get_feedback(db, feedback_id=feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    if len(response.answers) != len(feedback.questionnaires):
        raise HTTPException(status_code=400, detail="Number of answers does not match number of questionnaires")

    return crud.create_feedback_response(db=db, feedback_id=feedback_id, response=response)


@router.get("/{feedback_id}/analysis", response_model=schemas.FeedbackAnalysis)
def get_feedback_analysis(feedback_id: int, db: Session = Depends(get_db)):
    analysis = crud.analyze_feedback(db=db, feedback_id=feedback_id)
    if analysis is None:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return analysis
