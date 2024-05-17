from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "tbl_teachers"

    TeacherID = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Email = Column(String(100))
    # Other relevant teacher information
    assignments = relationship("HomeworkAssignment", back_populates="teacher")

class Student(Base):
    __tablename__ = "tbl_students"

    StudentID = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Email = Column(String(100))
    # Other relevant student information
    submissions = relationship("HomeworkSubmission", back_populates="student")
    grades = relationship("Grade", back_populates="student")

class Subject(Base):
    __tablename__ = "tbl_subjects"

    SubjectID = Column(Integer, primary_key=True)
    SubjectName = Column(String(100))
    assignments = relationship("HomeworkAssignment", back_populates="subject")

class HomeworkAssignment(Base):
    __tablename__ = "tbl_homework_assignments"

    AssignmentID = Column(Integer, primary_key=True)
    TeacherID = Column(Integer, ForeignKey("tbl_teachers.TeacherID"))
    SubjectID = Column(Integer, ForeignKey("tbl_subjects.SubjectID"))
    DueDate = Column(Date)
    Description = Column(Text)
    AdditionalInstructions = Column(Text)
    Attachments = Column(Text)
    teacher = relationship("Teacher", back_populates="assignments")
    subject = relationship("Subject", back_populates="assignments")
    submissions = relationship("HomeworkSubmission", back_populates="assignment")

class HomeworkSubmission(Base):
    __tablename__ = "tbl_homework_submissions"

    SubmissionID = Column(Integer, primary_key=True)
    StudentID = Column(Integer, ForeignKey("tbl_students.StudentID"))
    AssignmentID = Column(Integer, ForeignKey("tbl_homework_assignments.AssignmentID"))
    SubmissionDate = Column(Date)
    Status = Column(String(50))
    SubmittedAttachments = Column(Text)
    student = relationship("Student", back_populates="submissions")
    assignment = relationship("HomeworkAssignment", back_populates="submissions")
    grades = relationship("Grade", back_populates="submission")

class Grade(Base):
    __tablename__ = "tbl_grades"

    GradeID = Column(Integer, primary_key=True)
    AssignmentID = Column(Integer, ForeignKey("tbl_homework_assignments.AssignmentID"))
    StudentID = Column(Integer, ForeignKey("tbl_students.StudentID"))
    Grade = Column(DECIMAL(5, 2))
    Feedback = Column(Text)
    student = relationship("Student", back_populates="grades")
Base.metadata.create_all(bind= engine)