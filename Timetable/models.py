# models.py

from sqlalchemy import Column, ForeignKey, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .database import engine
Base = declarative_base()

class Shift(Base):
    __tablename__ = 'shifts'

    ShiftID = Column(Integer, primary_key=True)
    ShiftName = Column(String(255))
    StartTime = Column(Time)
    EndTime = Column(Time)

class Subject(Base):
    __tablename__ = 'subjects'

    SubjectID = Column(Integer, primary_key=True)
    SubjectName = Column(String(255))
    Department = Column(String(255))

class Teacher(Base):
    __tablename__ = 'teachers'

    TeacherID = Column(Integer, primary_key=True)
    TeacherName = Column(String(255))
    Department = Column(String(255))
    ContactInfo = Column(String(255))

class Class(Base):
    __tablename__ = 'classes'

    ClassID = Column(Integer, primary_key=True)
    ClassName = Column(String(255))
    Section = Column(String(255))
    ShiftID = Column(Integer, ForeignKey('shifts.ShiftID'))
    shift = relationship("Shift")

class Timetable(Base):
    __tablename__ = 'timetable'

    TimetableID = Column(Integer, primary_key=True)
    ClassID = Column(Integer, ForeignKey('classes.ClassID'))
    SubjectID = Column(Integer, ForeignKey('subjects.SubjectID'))
    TeacherID = Column(Integer, ForeignKey('teachers.TeacherID'))
    DayOfWeek = Column(String(255))
    PeriodNumber = Column(Integer)
    RoomNumber = Column(String(255))

Base.metadata.create_all(bind= engine)