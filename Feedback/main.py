from fastapi import APIRouter
from .database import database, engine, Base
from .feedback import user, feedback_form, question, response, objective

Base.metadata.create_all(bind=engine)

app = APIRouter()

app.include_router(user.router)
app.include_router(feedback_form.router)
app.include_router(question.router)
# app.include_router(feedback_session.router)
app.include_router(response.router)
app.include_router(objective.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
