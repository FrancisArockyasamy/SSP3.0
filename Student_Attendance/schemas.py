from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    student_name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int
    
    class Config:
        orm_mode = True

class AttendanceBase(BaseModel):
    student_id: int
    user_id: int
    attendance_date: str
    attendance_status_id: int
    attendance_entry_type_id: int
    late_details: Optional[str] = None
    other_details: Optional[str] = None

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    attendance_id: int
    
    class Config:
        orm_mode = True
