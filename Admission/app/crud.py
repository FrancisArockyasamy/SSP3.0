from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_admission_form(db: Session, form: schemas.AdmissionFormCreate):
    db_form = models.AdmissionForm(**form.dict())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

def create_form_field(db: Session, field: schemas.FormFieldCreate):
    db_field = models.FormField(**field.dict())
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field

def create_applicant(db: Session, applicant: schemas.ApplicantCreate):
    db_applicant = models.Applicant(**applicant.dict())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

def create_applicant_detail(db: Session, detail: schemas.ApplicantDetailCreate):
    db_detail = models.ApplicantDetail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def create_interview(db: Session, interview: schemas.InterviewCreate):
    db_interview = models.Interview(**interview.dict())
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview

def create_class(db: Session, cls: schemas.ClassCreate):
    db_class = models.Class(**cls.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def create_admission(db: Session, admission: schemas.AdmissionCreate):
    db_admission = models.Admission(**admission.dict())
    db.add(db_admission)
    db.commit()
    db.refresh(db_admission)
    return db_admission
