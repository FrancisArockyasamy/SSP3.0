from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from model import FeedbackSession
from typing import List

router = APIRouter()

# Create a new feedback session
@router.post("/feedback-sessions/", response_model=FeedbackSession)
async def create_feedback_session(session: FeedbackSession, db: Session = Depends(get_db)):
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

# Get all feedback sessions
@router.get("/feedback-sessions/", response_model=List[FeedbackSession])
async def get_feedback_sessions(db: Session = Depends(get_db)):
    return db.query(FeedbackSession).all()

# Get feedback session by ID
@router.get("/feedback-sessions/{session_id}", response_model=FeedbackSession)
async def get_feedback_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(FeedbackSession).filter(FeedbackSession.session_id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Feedback session not found")
    return session

# Update feedback session by ID
@router.put("/feedback-sessions/{session_id}", response_model=FeedbackSession)
async def update_feedback_session(session_id: int, session: FeedbackSession, db: Session = Depends(get_db)):
    existing_session = db.query(FeedbackSession).filter(FeedbackSession.session_id == session_id).first()
    if existing_session is None:
        raise HTTPException(status_code=404, detail="Feedback session not found")
    for key, value in session.dict().items():
        setattr(existing_session, key, value)
    db.commit()
    db.refresh(existing_session)
    return existing_session

# Delete feedback session by ID
@router.delete("/feedback-sessions/{session_id}")
async def delete_feedback_session(session_id: int, db: Session = Depends(get_db)):
    session = db.query(FeedbackSession).filter(FeedbackSession.session_id == session_id).first()
    if session is None:
        raise HTTPException(status_code=404, detail="Feedback session not found")
    db.delete(session)
    db.commit()
    return {"message": "Feedback session deleted successfully"}
