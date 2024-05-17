from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import model, schemas, database

router = APIRouter(prefix="/objectives", tags=["Objectives"])

@router.post("/", response_model=schemas.Objective)
async def create_objective(objective: schemas.ObjectiveCreate, db: Session = Depends(database.get_db)):
    db_objective = model.Objective(
        session_id=objective.session_id,
        objective_text=objective.objective_text
    )
    db.add(db_objective)
    db.commit()
    db.refresh(db_objective)
    return db_objective
