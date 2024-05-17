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


class MarkBase(BaseModel):
    mark_id: int
    exam_subject_id: int
    student_id: int
    marks: int 


class ExaminationCreate(BaseModel):
    exam_id : int
    exam_name : str
    exam_type :str
    class_id :int
    grading_system : str


class CreateClass(BaseModel):
    class_id:int
    class_name:str

class ExaminationCreate(BaseModel):
    pass

class ExaminationUpdate(BaseModel):
    pass

class Examination(BaseModel):
    exam_id: int


# Define schemas for other tables similarly
