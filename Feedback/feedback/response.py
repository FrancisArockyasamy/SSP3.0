from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model, schemas, database

router = APIRouter(prefix="/responses", tags=["Responses"])

@router.post("/", response_model=schemas.Response)
async def create_response(response: schemas.ResponseCreate, db: Session = Depends(database.get_db)):
    db_response = model.Response(
        session_id=response.session_id,
        question_id=response.question_id,
        response_text=response.response_text,
        response_rating=response.response_rating,
        user_id=1  # Replace with actual user_id
    )
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    return db_response
