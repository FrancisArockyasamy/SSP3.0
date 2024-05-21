from fastapi import FastAPI
from database import engine
from routers import feedback
import models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(feedback.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Fee Module API"}
