from pydantic import BaseModel
from typing import Optional

class Class(BaseModel):
  name: str
  grade_level: int
  section: str

class Subject(BaseModel):
  name: str
  description: str | None

class Staff(BaseModel):
  name: str
  role: str

class ClassSubject(BaseModel):
  # class_id: int
  subject_id: int

class ClassStaff(BaseModel):
  class_id: int
  subject_id:int
  staff_id: int

class Room(BaseModel):
  name: str
  capacity: int
  features: str | None

class ClassSchedule(BaseModel):
  class_id: int
  day: str
  room_id: int | None  # Optional room assignment


class ClassScheduleAllocation(BaseModel):
  class_id: int
  room_id: int
  date: str
  period: int
