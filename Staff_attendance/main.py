from fastapi import APIRouter
from .database import engine, SessionLocal, Base
from . import attendance


# Create FastAPI app instance
app = APIRouter()

# Include routers
app.include_router(attendance.router)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Staff Attendance API!"}
