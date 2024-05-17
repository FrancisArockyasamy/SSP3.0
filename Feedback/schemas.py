from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password_hash: str
    role: str

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class FeedbackFormCreate(BaseModel):
    title: str
    description: Optional[str] = None

class FeedbackForm(BaseModel):
    form_id: int
    title: str
    description: Optional[str] = None
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True

class QuestionCreate(BaseModel):
    question_text: str
    question_type: str

class Question(BaseModel):
    question_id: int
    form_id: int
    question_text: str
    question_type: str
    created_at: datetime

    class Config:
        from_attributes = True

class OptionCreate(BaseModel):
    option_text: str

class Option(BaseModel):
    option_id: int
    question_id: int
    option_text: str

    class Config:
        from_attributes = True

class FeedbackSessionCreate(BaseModel):
    form_id: int
    start_date: datetime
    end_date: datetime

class FeedbackSession(BaseModel):
    session_id: int
    form_id: int
    start_date: datetime
    end_date: datetime
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True

class ResponseCreate(BaseModel):
    session_id: int
    question_id: int
    response_text: Optional[str] = None
    response_rating: Optional[int] = None

class Response(BaseModel):
    response_id: int
    session_id: int
    user_id: int
    question_id: int
    response_text: Optional[str] = None
    response_rating: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

class ObjectiveCreate(BaseModel):
    session_id: int
    objective_text: str

class Objective(BaseModel):
    objective_id: int
    session_id: int
    objective_text: str
    created_at: datetime

    class Config:
        from_attributes = True
