from pydantic import BaseModel, EmailStr, constr, conint
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6)
    email: EmailStr
    full_name: constr(min_length=1, max_length=100)
    role: constr(min_length=3, max_length=50)

class AdmissionFormCreate(BaseModel):
    form_name: constr(min_length=1, max_length=100)
    created_by: conint(gt=0)

class FormFieldCreate(BaseModel):
    form_id: conint(gt=0)
    field_name: constr(min_length=1, max_length=100)
    field_type: constr(min_length=1, max_length=50)
    is_required: bool = True
    field_options: Optional[str]

class ApplicantCreate(BaseModel):
    user_id: conint(gt=0)
    application_status: Optional[str] = "Registered & Paid"

class ApplicantDetailCreate(BaseModel):
    applicant_id: conint(gt=0)
    field_id: conint(gt=0)
    field_value: constr(min_length=1)

class InterviewCreate(BaseModel):
    applicant_id: conint(gt=0)
    interview_date: datetime
    location: constr(min_length=1, max_length=100)
    panel_members: List[int]
    criteria: constr(min_length=1)

class ClassCreate(BaseModel):
    class_name: constr(min_length=1, max_length=100)
    seats_available: conint(gt=0)

class AdmissionCreate(BaseModel):
    applicant_id: conint(gt=0)
    class_id: conint(gt=0)
