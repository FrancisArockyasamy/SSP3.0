from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean,BigInteger
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'tbl_users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Student(Base):
    __tablename__ = 'tbl_students'
    student_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('tbl_users.user_id'), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey('tbl_classes.class_id'), nullable=False)

class Class(Base):
    __tablename__ = 'tbl_classes'
    class_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=False)

class Subject(Base):
    __tablename__ = 'tbl_subjects'
    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, nullable=False)

class Examination(Base):
    __tablename__ = 'tbl_examinations'
    exam_id = Column(Integer, primary_key=True, index=True)
    exam_name = Column(String, nullable=False)
    exam_type = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey('tbl_classes.class_id'), nullable=False)
    grading_system = Column(String, nullable=False)

class ExamSubject(Base):
    __tablename__ = 'tbl_exam_subjects'
    exam_subject_id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey('tbl_examinations.exam_id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('tbl_subjects.subject_id'), nullable=False)

class ExamSetting(Base):
    __tablename__ = 'tbl_exam_settings'
    setting_id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey('tbl_examinations.exam_id'), nullable=False)
    mark_entry_method = Column(String, nullable=False)

class OptionalSubject(Base):
    __tablename__ = 'tbl_optional_subjects'
    option_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('tbl_subjects.subject_id'), nullable=False)

class ExamAttendance(Base):
    __tablename__ = 'tbl_exam_attendance'
    attendance_id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey('tbl_examinations.exam_id'), nullable=False)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    attendance_status = Column(Boolean, nullable=False)

class Mark(Base):
    __tablename__ = 'tbl_marks'
    mark_id = Column(Integer, primary_key=True, index=True)
    exam_subject_id = Column(Integer, ForeignKey('tbl_exam_subjects.exam_subject_id'), nullable=False)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    marks = Column(Integer, nullable=False)

class CoCurricularGrade(Base):
    __tablename__ = 'tbl_co_curricular_grades'
    grade_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    activity_name = Column(String, nullable=False)
    grade = Column(String, nullable=False)

class PhysicalMetric(Base):
    __tablename__ = 'tbl_physical_metrics'
    metric_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    term = Column(String, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)

class Result(Base):
    __tablename__ = 'tbl_results'
    result_id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey('tbl_examinations.exam_id'), nullable=False)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    result_status = Column(String, nullable=False)

class ProgressCard(Base):
    __tablename__ = 'tbl_progress_cards'
    progress_card_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    exam_id = Column(Integer, ForeignKey('tbl_examinations.exam_id'), nullable=False)
    template_id = Column(Integer, nullable=False)
    generated_card = Column(BigInteger, nullable=False)

class HallTicket(Base):
    __tablename__ = 'tbl_hall_tickets'
    hall_ticket_id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey('tbl_examinations.exam_id'), nullable=False)
    student_id = Column(Integer, ForeignKey('tbl_students.student_id'), nullable=False)
    generated_ticket = Column(BigInteger, nullable=False)
