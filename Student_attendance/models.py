from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)
    attendance = relationship('Attendance', back_populates='student')

class Attendance(Base):
    __tablename__ = 'attendance'

    attendance_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    attendance_date = Column(Date)
    attendance_status = Column(String)
    attendance_reason = Column(String)
    attendance_duration = Column(Integer)

    student = relationship('Student', back_populates='attendance')
