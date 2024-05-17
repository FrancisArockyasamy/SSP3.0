from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    role: str = Field(..., min_length=3, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    class_id: int

class StudentCreate(StudentBase):
    user_id: int

class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True

# Define schemas for other tables similarly
