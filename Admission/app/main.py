from fastapi import FastAPI
from .database import engine, Base
from .routers import users, admission_forms, form_fields, applicants, applicant_details, interviews, classes, admissions

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(admission_forms.router, prefix="/admission_forms", tags=["admission_forms"])
app.include_router(form_fields.router, prefix="/form_fields", tags=["form_fields"])
app.include_router(applicants.router, prefix="/applicants", tags=["applicants"])
app.include_router(applicant_details.router, prefix="/applicant_details", tags=["applicant_details"])
app.include_router(interviews.router, prefix="/interviews", tags=["interviews"])
app.include_router(classes.router, prefix="/classes", tags=["classes"])
app.include_router(admissions.router, prefix="/admissions", tags=["admissions"])
