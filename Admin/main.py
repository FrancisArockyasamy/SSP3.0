from fastapi import APIRouter
from .APIs import admin
from .models.admin import Base
from .settings.db import engine

Base.metadata.create_all(bind=engine)

app = APIRouter(
)

@app.get('/')
def root():
    return {"message": "SSP 3.0 API service is running"}

# include api routes with main app
app.include_router(admin.app)
app.include_router(admin.app1)
app.include_router(admin.app2)
app.include_router(admin.app3)

