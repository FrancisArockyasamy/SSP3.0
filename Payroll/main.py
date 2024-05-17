from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .import models, schemas
from .database import get_db, engine
from .models import Base

Base.metadata.create_all(bind= engine)

app = APIRouter(
    tags=["Payroll"]
)

# Dependency for getting the database session


@app.post("/payroll_structures/", response_model=schemas.PayrollStructure)
def create_payroll_structure(structure: schemas.PayrollStructureBase, db: Session = Depends(get_db)):
    db_structure = models.PayrollStructure(**structure.dict())
    db.add(db_structure)
    db.commit()
    db.refresh(db_structure)
    return db_structure

@app.post("/salary_components/", response_model=schemas.SalaryComponent)
def create_salary_component(component: schemas.SalaryComponentBase, db: Session = Depends(get_db)):
    db_component = models.SalaryComponent(**component.dict())
    db.add(db_component)
    db.commit()
    db.refresh(db_component)
    return db_component

@app.post("/payroll_groups/", response_model=schemas.PayrollGroup)
def create_payroll_group(group: schemas.PayrollGroupBase, db: Session = Depends(get_db)):
    db_group = models.PayrollGroup(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group
