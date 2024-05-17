from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
# from sqlalchemy.sql import CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from sqlalchemy import CheckConstraint


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(255))
    role = Column(String(20),  ("role IN ('HR Admin', 'Staff')"))
    created_at = Column(DateTime, default=func.now())

class FeedbackForm(Base):
    __tablename__ = "feedback_forms"
    form_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text)
    created_by = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime, default=func.now())

class Question(Base):
    __tablename__ = "questions"
    question_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("feedback_forms.form_id", ondelete="CASCADE"))
    question_text = Column(Text)
    question_type = Column(String(20), CheckConstraint("question_type IN ('Multiple Choice', 'Rating Scale', 'Open-ended')"))
    created_at = Column(DateTime, default=func.now())

class Option(Base):
    __tablename__ = "options"
    option_id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.question_id", ondelete="CASCADE"))
    option_text = Column(String(255))

class FeedbackSession(Base):
    __tablename__ = "feedback_sessions"
    session_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("feedback_forms.form_id", ondelete="CASCADE"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_by = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime, default=func.now())

class Response(Base):
    __tablename__ = "responses"
    response_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("feedback_sessions.session_id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    question_id = Column(Integer, ForeignKey("questions.question_id"))
    response_text = Column(Text, nullable=True)
    response_rating = Column(Integer, CheckConstraint("response_rating BETWEEN 1 AND 5"), nullable=True)
    created_at = Column(DateTime, default=func.now())

class Objective(Base):
    __tablename__ = "objectives"
    objective_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("feedback_sessions.session_id", ondelete="CASCADE"))
    objective_text = Column(Text)
    created_at = Column(DateTime, default=func.now())
