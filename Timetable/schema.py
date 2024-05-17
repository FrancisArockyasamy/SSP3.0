# schema.py

from pydantic import BaseModel
from typing import Optional

from datetime import datetime, time

class ShiftBase(BaseModel):
    ShiftName: str
    StartTime: Optional[time] = None
    EndTime: Optional[time] = None

class ShiftCreate(ShiftBase):
    pass

# Define a response model that aligns with your expected output
class ShiftResponse(BaseModel):
    ShiftID: int
    ShiftName: str
    StartTime: time
    EndTime: time

class SubjectBase(BaseModel):
    SubjectName: str
    Department: Optional[str]

class SubjectCreate(SubjectBase):
    pass

class SubjectResponse(BaseModel):
    SubjectID : int
    SubjectName :str
    Department :str

class TeacherBase(BaseModel):
    TeacherName: str
    Department: Optional[str]
    ContactInfo: Optional[str]

class TeacherCreate(TeacherBase):
    pass

class ClassBase(BaseModel):
    ClassName: str
    Section: str
    ShiftID: int

class ClassCreate(ClassBase):
    pass

class TimetableBase(BaseModel):
    ClassID: int
    SubjectID: int
    TeacherID: int
    DayOfWeek: str
    PeriodNumber: int
    RoomNumber: str

class TimetableCreate(TimetableBase):
    pass
