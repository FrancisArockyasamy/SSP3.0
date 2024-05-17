from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'tbl_users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    password_hash = Column(String(128), nullable=False)
    email = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)
    
    __table_args__ = (
        CheckConstraint("role IN ('HR Admin', 'Staff')", name='check_role'),
    )

    feedback_forms = relationship("FeedbackForm", back_populates="creator")
    responses = relationship("Response", back_populates="user")

class FeedbackForm(Base):
    __tablename__ = 'tbl_feedback_forms'

    form_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    created_by = Column(Integer, ForeignKey('tbl_users.user_id'))
    created_at = Column(DateTime, server_default="now()")

    creator = relationship("User", back_populates="feedback_forms")
    questions = relationship("Question", back_populates="form")
    objectives = relationship("Objective", back_populates="form")
    sessions = relationship("FeedbackSession", back_populates="form")

class Question(Base):
    __tablename__ = 'tbl_questions'

    question_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey('tbl_feedback_forms.form_id'))
    question_text = Column(Text, nullable=False)
    question_type = Column(String(20), nullable=False)
    order = Column(Integer, nullable=False)

    form = relationship("FeedbackForm", back_populates="questions")
    options = relationship("QuestionOption", back_populates="question")

class QuestionOption(Base):
    __tablename__ = 'tbl_question_options'

    option_id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('tbl_questions.question_id'))
    option_text = Column(String(100), nullable=False)

    question = relationship("Question", back_populates="options")

class Objective(Base):
    __tablename__ = 'tbl_objectives'

    objective_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey('tbl_feedback_forms.form_id'))
    objective_text = Column(Text, nullable=False)

    form = relationship("FeedbackForm", back_populates="objectives")

class FeedbackSession(Base):
    __tablename__ = 'tbl_feedback_sessions'

    session_id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey('tbl_feedback_forms.form_id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    form = relationship("FeedbackForm", back_populates="sessions")
    responses = relationship("Response", back_populates="session")

class Response(Base):
    __tablename__ = 'tbl_responses'

    response_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('tbl_feedback_sessions.session_id'))
    user_id = Column(Integer, ForeignKey('tbl_users.user_id'))
    submitted_at = Column(DateTime, server_default="now()")

    session = relationship("FeedbackSession", back_populates="responses")
    user = relationship("User", back_populates="responses")
    answers = relationship("Answer", back_populates="response")

class Answer(Base):
    __tablename__ = 'tbl_answers'

    answer_id = Column(Integer, primary_key=True, index=True)
    response_id = Column(Integer, ForeignKey('tbl_responses.response_id'))
    question_id = Column(Integer, ForeignKey('tbl_questions.question_id'))
    answer_text = Column(Text)

    response = relationship("Response", back_populates="answers")
    question = relationship("Question")
