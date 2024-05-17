from fastapi import FastAPI
from .database import engine
from . import models
from .routers import users, students

# models.Base.metadata.drop_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(students.router)
