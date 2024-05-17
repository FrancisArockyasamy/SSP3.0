from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, database,model

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(model.User).filter(model.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = user.password_hash # Replace with password hashing
    db_user = model.User(
        username=user.username, email=user.email, password_hash=hashed_password, role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
