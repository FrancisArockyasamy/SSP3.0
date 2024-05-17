from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import Base, engine

Base = declarative_base()

class Student(Base):
    __tablename__ = "tbl_students"

    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)
    address = Column(String)
    class_id = Column(Integer, ForeignKey("tbl_classes.class_id"))

    classes = relationship("Class", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    attendance = relationship("Attendance", back_populates="student")
    remarks = relationship("Remark", back_populates="student")
    sms_usage = relationship("SMSUsage", back_populates="student")
    progress_cards = relationship("ProgressCard", back_populates="student")
    fee_payments = relationship("FeePayment", back_populates="student")


class Class(Base):
    __tablename__ = "tbl_classes"

    class_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False, unique=True)
    class_teacher_id = Column(Integer, ForeignKey("tbl_teachers.teacher_id"))

    teacher = relationship("Teacher", back_populates="classes")
    students = relationship("Student", back_populates="classes")
    homework = relationship("Homework", back_populates="class_")
    attendance = relationship("Attendance", back_populates="class_")


class Teacher(Base):
    __tablename__ = "tbl_teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String)

    classes = relationship("Class", back_populates="teacher")


class Subject(Base):
    __tablename__ = "tbl_subjects"

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, nullable=False, unique=True)
    homework = relationship("Homework", back_populates="subject")
    grades = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = "tbl_grades"

    grade_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.student_id"))
    subject_id = Column(Integer, ForeignKey("tbl_subjects.subject_id"))
    grade_value = Column(Float)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    progress_cards = relationship("ProgressCard", back_populates="grade")  
class Attendance(Base):
    __tablename__ = "tbl_attendance"

    attendance_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.student_id"))
    class_id = Column(Integer, ForeignKey("tbl_classes.class_id"))
    date = Column(Date)
    status = Column(String)

    student = relationship("Student", back_populates="attendance")
    class_ = relationship("Class", back_populates="attendance")


class Homework(Base):
    __tablename__ = "tbl_homework"

    homework_id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("tbl_classes.class_id"))
    subject_id = Column(Integer, ForeignKey("tbl_subjects.subject_id"))
    deadline = Column(Date)
    assignment_details = Column(Text)
    submission_status = Column(String)

    class_ = relationship("Class", back_populates="homework")
    subject = relationship("Subject", back_populates="homework")


class Remark(Base):
    __tablename__ = "tbl_remarks"

    remark_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.student_id"))
    remarks_details = Column(Text)
    remark_date = Column(Date)

    student = relationship("Student", back_populates="remarks")


class SMSUsage(Base):
    __tablename__ = "tbl_sms_usage"

    sms_usage_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.student_id"))
    messages_sent = Column(Integer)
    remaining_credits = Column(Integer)

    student = relationship("Student", back_populates="sms_usage")


class ProgressCard(Base):
    __tablename__ = "tbl_progress_cards"

    progress_card_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.student_id"))
    term = Column(String)
    academic_year = Column(String)
    grade_id = Column(Integer, ForeignKey("tbl_grades.grade_id"))

    student = relationship("Student", back_populates="progress_cards")
    grade = relationship("Grade", back_populates="progress_cards")


class FeePayment(Base):
    __tablename__ = "tbl_fee_payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.student_id"))
    payment_date = Column(Date)
    amount = Column(Float)
    payment_method = Column(String)
    receipt_url = Column(String)

    student = relationship("Student", back_populates="fee_payments")

Base.metadata.create_all(engine)