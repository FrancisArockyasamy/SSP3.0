from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, JSON,Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

Base = declarative_base()
# Define SQLAlchemy models
class SubjectChapters(Base):
    __tablename__ = "tbl_subject_chapters"

    id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, nullable=False)
    chapter_name = Column(String, nullable=False)

class LessonPlans(Base):
    __tablename__ = "tbl_lesson_plans"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, nullable=False)
    sub_topic = Column(String, nullable=False)
    objectives = Column(String, nullable=False)
    teaching_methods = Column(String, nullable=False)
    resources = Column(String, nullable=False)
    assessments = Column(String, nullable=False)

class ImportedLessonPlans(Base):
    __tablename__ = "tbl_imported_lesson_plans"

    id = Column(Integer, primary_key=True, index=True)
    lesson_plan_id = Column(Integer, nullable=False)
    source_url = Column(String, nullable=False)

class YearPlan(Base):
    __tablename__ = "tbl_year_plan"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(String, nullable=False)
    planned_chapters = Column(JSON, nullable=False)
    status = Column(String, nullable=False)

class WeeklyPlans(Base):
    __tablename__ = "tbl_weekly_plans"

    id = Column(Integer, primary_key=True, index=True)
    year_plan_id = Column(Integer, nullable=False)
    week_number = Column(Integer, nullable=False)
    planned_lessons = Column(JSON, nullable=False)

class StaffLessonPlans(Base):
    __tablename__ = "tbl_staff_lesson_plans"

    id = Column(Integer, primary_key=True, index=True)
    lesson_plan_id = Column(Integer, nullable=False)
    staff_id = Column(Integer, nullable=False)

class LessonObservations(Base):
    __tablename__ = "tbl_lesson_observations"

    id = Column(Integer, primary_key=True, index=True)
    observer_id = Column(Integer, nullable=False)
    lesson_plan_id = Column(Integer, nullable=False)
    objectives = Column(String, nullable=False)
    questions = Column(String, nullable=False)

class FeedbackAssessments(Base):
    __tablename__ = "tbl_feedback_assessments"

    id = Column(Integer, primary_key=True, index=True)
    observation_id = Column(Integer, nullable=False)
    feedback = Column(String, nullable=False)
    assessment = Column(String, nullable=False)

# Create tables in the database
Base.metadata.create_all(bind=engine)
