from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schema

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/visitors/", response_model=schema.Visitor)
def create_visitor(visitor: schema.VisitorCreate, db: Session = Depends(get_db)):
    db_visitor = models.Visitor(**visitor.dict())
    db.add(db_visitor)
    db.commit()
    db.refresh(db_visitor)
    return db_visitor

@app.get("/visitors/{visitor_id}", response_model=schema.Visitor)
def get_visitor(visitor_id: int, db: Session = Depends(get_db)):
    db_visitor = db.query(models.Visitor).filter(models.Visitor.visitor_id == visitor_id).first()
    if db_visitor is None:
        raise HTTPException(status_code=404, detail="Visitor not found")
    return db_visitor
