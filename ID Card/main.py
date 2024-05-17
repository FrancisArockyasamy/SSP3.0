from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# FastAPI app instance
app = FastAPI()

# SQLAlchemy database setup
SQLALCHEMY_DATABASE_URL = "postgresql://root:root@localhost/idcard"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Pydantic models for data validation
class TemplateBase(BaseModel):
    template_name: str

class TemplateCreate(TemplateBase):
    pass

class Template(TemplateBase):
    template_id: int

    class Config:
        orm_mode = True

class IDCardBase(BaseModel):
    orientation: str
    background_image: str
    num_student_copies: int
    num_staff_copies: int

class IDCardCreate(IDCardBase):
    template_id: int

class IDCard(IDCardBase):
    id_card_id: int
    template: Template

    class Config:
        orm_mode = True

# SQLAlchemy models
class Template(Base):
    __tablename__ = "template"

    template_id = Column(Integer, primary_key=True, index=True)
    template_name = Column(String, index=True)

    id_cards = relationship("IDCard", back_populates="template")

class IDCard(Base):
    __tablename__ = "id_card"

    id_card_id = Column(Integer, primary_key=True, index=True)
    orientation = Column(String, index=True)
    background_image = Column(String)
    num_student_copies = Column(Integer)
    num_staff_copies = Column(Integer)
    template_id = Column(Integer, ForeignKey("template.template_id"))

    template = relationship("Template", back_populates="id_cards")

Base.metadata.create_all(engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoints
@app.post("/template/", response_model=None)
def create_template(template: TemplateCreate, db: Session = Depends(get_db)):
    db_template = Template(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

@app.post("/id_card/", response_model=None)
def create_id_card(id_card: IDCardCreate, db: Session = Depends(get_db)):
    db_id_card = IDCard(**id_card.dict())
    db.add(db_id_card)
    db.commit()
    db.refresh(db_id_card)
    return db_id_card
