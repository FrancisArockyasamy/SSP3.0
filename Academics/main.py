from fastapi import FastAPI ,Depends
from sqlalchemy.orm import Session
from db import get_db , engine
from models import Base
from routes import classes , subjects , staffs , class_wise_subjects , class_wise_staff_allocation , rooms , class_room_allotement


app = FastAPI(title="SSP3.0")
app.include_router(classes.app)
app.include_router(subjects.app)
app.include_router(staffs.app)
app.include_router(class_wise_subjects.app)
app.include_router(class_wise_staff_allocation.app)
app.include_router(rooms.app)
app.include_router(class_room_allotement.app)

Base.metadata.create_all(bind=engine)

# Example usage in a route (assuming a model is defined)
@app.get("/")
def root():
    return "Root function works Successfully"

