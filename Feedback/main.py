from fastapi import FastAPI, APIRouter
from .database import engine
from . import models
from .routers import feedback


models.Base.metadata.create_all(bind=engine)
app = APIRouter()
app.include_router(feedback.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the School Fee Module API"}
