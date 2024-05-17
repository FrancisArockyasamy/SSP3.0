from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from pydantic import BaseModel
from sqlalchemy import create_engine,Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import Session
import io
import pandas as pd
from fastapi.responses import StreamingResponse
from typing import List
from sqlalchemy_utils import database_exists, create_database

# PostgreSQL database connection
DATABASE_URL = "postgresql://root:Aero%400031@localhost/alumni1"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy models
class AcademicYear(Base):
    __tablename__ = "academic_year"

    academic_year_id = Column(Integer, primary_key=True, index=True)
    academic_year = Column(Integer, nullable=False)

class Alumni(Base):
    __tablename__ = "alumni"

    alumni_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    contact_email = Column(String)
    contact_phone = Column(String)
    career_updates = Column(String)
    other_details = Column(String)

    academic_years = relationship("AlumniAcademic", back_populates="alumni")

class AlumniAcademic(Base):
    __tablename__ = "alumni_academic"

    alumni_academic_id = Column(Integer, primary_key=True, index=True)
    alumni_id = Column(Integer, ForeignKey("alumni.alumni_id"))
    academic_year_id = Column(Integer, ForeignKey("academic_year.academic_year_id"))

    alumni = relationship("Alumni", back_populates="academic_years")
    academic_year = relationship("AcademicYear")


if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)
# Base.metadata.create_all(bind=engine)


# Pydantic models for data validation
class AcademicYearCreate(BaseModel):
    academic_year: int

class AlumniCreate(BaseModel):
    first_name: str
    last_name: str
    contact_email: str 
    contact_phone: str 
    career_updates: str 
    other_details: str 

class AlumniUpdate(BaseModel):
    contact_email: str 
    contact_phone: str 
    career_updates: str 
    other_details: str 

class Alumni1(BaseModel):
    alumni_id: int
    first_name: str
    last_name: str
    contact_email: str
    contact_phone: str
    career_updates: str
    other_details: str

    class Config:
        orm_mode = True

class AlumniBulkCreate(BaseModel):
    alumni_data: List[AlumniCreate]

Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API routes
@app.post("/academic_years/", response_model=AcademicYearCreate)
def create_academic_year(academic_year: AcademicYearCreate, db: Session = Depends(get_db)):
    db_academic_year = AcademicYear(**academic_year.dict())
    db.add(db_academic_year)
    db.commit()
    db.refresh(db_academic_year)
    return db_academic_year

@app.post("/alumni/", response_model=AlumniCreate)
def create_alumni(alumni: AlumniCreate, db: Session = Depends(get_db)):
    db_alumni = Alumni(**alumni.dict())
    db.add(db_alumni)
    db.commit()
    db.refresh(db_alumni)
    return db_alumni

@app.get("/alumni/{alumni_id}", response_model=Alumni1)
def get_alumni(alumni_id: int, db: Session = Depends(get_db)):
    return db.query(Alumni).filter(Alumni.alumni_id == alumni_id).first()

@app.put("/alumni/{alumni_id}", response_model=Alumni1)
def update_alumni(alumni_id: int, alumni_update: AlumniUpdate, db: Session = Depends(get_db)):
    db_alumni = db.query(Alumni).filter(Alumni.alumni_id == alumni_id).first()
    if db_alumni is None:
        raise HTTPException(status_code=404, detail="Alumni not found")
    for key, value in alumni_update.dict(exclude_unset=True).items():
        setattr(db_alumni, key, value)
    db.commit()
    db.refresh(db_alumni)
    return db_alumni

@app.get("/alumni/template/")
def download_template():
    # Create a DataFrame with column names matching the AlumniCreate Pydantic model
    template_df = pd.DataFrame(columns=["first_name", "last_name", "contact_email", "contact_phone", "career_updates", "other_details"])
    
    # Convert DataFrame to Excel file
    excel_file = io.BytesIO()
    with pd.ExcelWriter(excel_file, engine="xlsxwriter", mode="w") as writer:
        template_df.to_excel(writer, index=False, sheet_name="Alumni Template")
    
    excel_file.seek(0)
    
    # Return the Excel file as a streaming response
    return StreamingResponse(io.BytesIO(excel_file.read()), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=alumni_template.xlsx"})

# @app.post("/alumni/bulk/", response_model=List[Alumni1])
# def bulk_create_alumni(alumni_data: AlumniBulkCreate, db: Session = Depends(get_db)):
#     alumni_objects = [Alumni(**data.dict()) for data in alumni_data.alumni_data]
#     db.add_all(alumni_objects)
#     db.commit()
#     return alumni_objects

@app.post("/alumni/bulk/")
def bulk_create_alumni(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Read the uploaded file
    df = pd.read_excel(file.file)  # Assuming the file is in Excel format
    
    # Convert DataFrame to a list of dictionaries
    alumni_data = df.to_dict(orient="records")
    
    # Create Alumni objects from the data
    alumni_objects = [Alumni(**data) for data in alumni_data]
    
    # Add Alumni objects to the database session and commit
    db.add_all(alumni_objects)
    db.commit()
    
    return {"message": f"{len(alumni_objects)} records inserted successfully"}