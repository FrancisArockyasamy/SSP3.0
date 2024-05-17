from sqlalchemy import Column, Integer, String, ForeignKey, Text , Date , UniqueConstraint
from typing import Optional 
from datetime import datetime , date
from sqlalchemy.orm import relationship
from db import Base



class Class(Base):
  __tablename__ = "classes"

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  grade_level = Column(Integer)
  section = Column(String(255))


class Subject(Base):
  __tablename__ = "subjects"

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  description = Column(Text)


class Staff(Base):
  __tablename__ = "staff"

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  role = Column(String(255))


class ClassSubject(Base):
  __tablename__ = "class_subjects"

  id = Column(Integer, primary_key=True)
  class_id = Column(Integer, ForeignKey("classes.id"))
  subject_id = Column(Integer, ForeignKey("subjects.id"))


class ClassStaff(Base):
  __tablename__ = "class_staff"

  id = Column(Integer, primary_key=True)
  class_id = Column(Integer, ForeignKey("classes.id"))
  subject_id = Column(Integer, ForeignKey("subjects.id"))
  staff_id = Column(Integer, ForeignKey("staff.id"))


class Room(Base):
  __tablename__ = "rooms"

  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  capacity = Column(Integer)
  features = Column(Text)


class ClassScheduleAllocation(Base):
    __tablename__ = "class_schedule_allocations"

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    date = Column(Date, nullable=False)
    period = Column(Integer, nullable=False)  # Assuming period is an integer (e.g., 1 for period 1)
    __table_args__ = (UniqueConstraint('class_id', 'date', 'period'),)

 
 
 
 
 
#   def __repr__(self):
#     return f"ClassSchedule(id={self.id}, class_id={self.class_id}, day='{self.day}', start_time='{self.start_time}', end_time='{self.end_time}', room_id={self.room_id})"