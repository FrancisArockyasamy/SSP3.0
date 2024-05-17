from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, TIMESTAMP, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "tbl_users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class AdmissionForm(Base):
    __tablename__ = "tbl_admission_forms"
    form_id = Column(Integer, primary_key=True, index=True)
    form_name = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey('tbl_users.user_id'))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class FormField(Base):
    __tablename__ = "tbl_form_fields"
    field_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey('tbl_admission_forms.form_id'))
    field_name = Column(String, nullable=False)
    field_type = Column(String, nullable=False)
    is_required = Column(Boolean, default=True)
    field_options = Column(Text)

class Applicant(Base):
    __tablename__ = "tbl_applicants"
    applicant_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('tbl_users.user_id'))
    application_status = Column(String, default="Registered & Paid")
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow)

class ApplicantDetail(Base):
    __tablename__ = "tbl_applicant_details"
    detail_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey('tbl_applicants.applicant_id'))
    field_id = Column(Integer, ForeignKey('tbl_form_fields.field_id'))
    field_value = Column(Text, nullable=False)

class Interview(Base):
    __tablename__ = "tbl_interviews"
    interview_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey('tbl_applicants.applicant_id'))
    interview_date = Column(TIMESTAMP, nullable=False)
    location = Column(String, nullable=False)
    panel_members = Column(ARRAY(Integer), nullable=False)  # Array of user_ids
    criteria = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

class Class(Base):
    __tablename__ = "tbl_classes"
    class_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False)
    seats_available = Column(Integer, nullable=False)

class Admission(Base):
    __tablename__ = "tbl_admissions"
    admission_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey('tbl_applicants.applicant_id'))
    class_id = Column(Integer, ForeignKey('tbl_classes.class_id'))
    admitted_at = Column(TIMESTAMP, default=datetime.utcnow)
