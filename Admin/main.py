from fastapi import FastAPI
from APIs import admin

app = FastAPI(
    title="SSP-3.0 API",
    version="1.0"
)

@app.get('/')
def root():
    return {"message": "SSP 3.0 API service is running"}

# include api routes with main app
app.include_router(admin.app)
app.include_router(admin.app1)
app.include_router(admin.app2)
app.include_router(admin.app3)

