from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    objectives = Column(Text)

    questionnaires = relationship("Questionnaire", back_populates="feedback")
    responses = relationship("FeedbackResponse", back_populates="feedback")

class Questionnaire(Base):
    __tablename__ = 'questionnaires'

    id = Column(Integer, primary_key=True, index=True)
    feedback_id = Column(Integer, ForeignKey('feedbacks.id'))
    question_text = Column(Text)
    question_type = Column(String)

    feedback = relationship("Feedback", back_populates="questionnaires")
    responses = relationship("QuestionnaireResponse", back_populates="questionnaire")

class FeedbackResponse(Base):
    __tablename__ = 'feedback_responses'

    id = Column(Integer, primary_key=True, index=True)
    feedback_id = Column(Integer, ForeignKey('feedbacks.id'))
    participant = Column(String, index=True)
    responses = relationship("QuestionnaireResponse", back_populates="feedback_response")

    feedback = relationship("Feedback", back_populates="responses")

class QuestionnaireResponse(Base):
    __tablename__ = 'questionnaire_responses'

    id = Column(Integer, primary_key=True, index=True)
    feedback_response_id = Column(Integer, ForeignKey('feedback_responses.id'))
    questionnaire_id = Column(Integer, ForeignKey('questionnaires.id'))
    answer = Column(Text)

    feedback_response = relationship("FeedbackResponse", back_populates="responses")
    questionnaire = relationship("Questionnaire", back_populates="responses")
