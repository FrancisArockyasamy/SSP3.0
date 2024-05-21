from pydantic import BaseModel
from typing import List, Optional

class QuestionnaireBase(BaseModel):
    question_text: str
    question_type: str

class QuestionnaireCreate(QuestionnaireBase):
    pass

class Questionnaire(QuestionnaireBase):
    id: int
    feedback_id: int

    class Config:
        orm_mode: True

class FeedbackBase(BaseModel):
    title: str
    description: Optional[str] = None
    objectives: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    questionnaires: List[QuestionnaireCreate] = []

class Feedback(FeedbackBase):
    id: int
    questionnaires: List[Questionnaire] = []

    class Config:
        orm_mode: True

class FeedbackResponseBase(BaseModel):
    participant: str

class FeedbackResponseCreate(FeedbackResponseBase):
    answers: List[str]

class FeedbackResponse(FeedbackResponseBase):
    id: int
    feedback_id: int
    answers: List[str]

    class Config:
        orm_mode: True

class FeedbackAnalysis(BaseModel):
    feedback_id: int
    analysis: dict
