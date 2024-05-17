from fastapi import FastAPI
from Admin import main
from Academics import main as academic_main
from Admission.app import main as admission_main

app= FastAPI(
    title="SSP-3.0 API"
)

for i in [main, academic_main]:
    app.include_router(i.app)
