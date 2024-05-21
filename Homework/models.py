from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

Base = declarative_base()

class Teacher(Base):
    __tablename__ = "tbl_teachers"

    teacherID = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(100))
   
    assignments = relationship("HomeworkAssignment", back_populates="teacher")

class Student(Base):
    __tablename__ = "tbl_students"

    studentID = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(100))
 
    submissions = relationship("HomeworkSubmission", back_populates="student")
    grades = relationship("Grade", back_populates="student")

class Subject(Base):
    __tablename__ = "tbl_subjects"

    subjectID = Column(Integer, primary_key=True)
    subjectName = Column(String(100))
    assignments = relationship("HomeworkAssignment", back_populates="subject")

class HomeworkAssignment(Base):
    __tablename__ = "tbl_homework_assignments"

    assignmentID = Column(Integer, primary_key=True, index=True)
    teacherID = Column(Integer, ForeignKey("tbl_teachers.teacherID"))
    subjectID = Column(Integer, ForeignKey("tbl_subjects.subjectID"))
    dueDate = Column(Date)
    description = Column(Text, nullable=True)
    additionalInstructions = Column(Text, nullable=True)
    attachments = Column(Text, nullable=True)

    teacher = relationship("Teacher", back_populates="assignments")
    subject = relationship("Subject", back_populates="assignments")
    submissions = relationship("HomeworkSubmission", back_populates="assignment")

class HomeworkSubmission(Base):
    __tablename__ = "tbl_homework_submissions"

    submissionID = Column(Integer, primary_key=True)
    studentID = Column(Integer, ForeignKey("tbl_students.studentID"))
    assignmentID = Column(Integer, ForeignKey("tbl_homework_assignments.assignmentID"))
    submissionDate = Column(Date)
    status = Column(String(50))
    submittedAttachments = Column(Text)
    student = relationship("Student", back_populates="submissions")
    assignment = relationship("HomeworkAssignment", back_populates="submissions")
    grades = relationship("Grade", back_populates="submission")

class Grade(Base):
    __tablename__ = "tbl_grades"

    gradeID = Column(Integer, primary_key=True)
    assignmentID = Column(Integer, ForeignKey("tbl_homework_assignments.assignmentID"))
    studentID = Column(Integer, ForeignKey("tbl_students.studentID"))
    submissionID = Column(Integer, ForeignKey("tbl_homework_submissions.submissionID")) 

    grade = Column(DECIMAL(5, 2))
    feedback = Column(Text)

    submission = relationship("HomeworkSubmission", back_populates="grades")
    student = relationship("Student", back_populates="grades")

Base.metadata.create_all(bind= engine)