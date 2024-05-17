from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class SubjectChapterCreate(BaseModel):
    subject_name: str = Field(..., title="Subject Name", min_length=1, max_length=255)
    chapter_name: str = Field(..., title="Chapter Name", min_length=1, max_length=255)

class LessonPlanCreate(BaseModel):
    chapter_id: int
    sub_topic: str = Field(..., title="Sub Topic", min_length=1, max_length=255)
    objectives: str = Field(..., title="Objectives", min_length=1)
    teaching_methods: str = Field(..., title="Teaching Methods", min_length=1)
    resources: str = Field(..., title="Resources", min_length=1)
    assessments: str = Field(..., title="Assessments", min_length=1)

class ImportedLessonPlanCreate(BaseModel):
    lesson_plan_id: int
    source_url: str = Field(..., title="Source URL", min_length=1, max_length=255)

class YearPlanCreate(BaseModel):
    year: str
    planned_chapters: List[int]
    status: str = Field(..., title="Status", min_length=1, max_length=255)

class WeeklyPlanCreate(BaseModel):
    year_plan_id: int
    week_number: int
    planned_lessons: List[int]

class StaffLessonPlanCreate(BaseModel):
    lesson_plan_id: int
    staff_id: int

class LessonObservationCreate(BaseModel):
    observer_id: int
    lesson_plan_id: int
    objectives: str = Field(..., title="Objectives", min_length=1)
    questions: str = Field(..., title="Questions", min_length=1)

class FeedbackAssessmentCreate(BaseModel):
    observation_id: int
    feedback: str = Field(..., title="Feedback", min_length=1)
    assessment: str = Field(..., title="Assessment", min_length=1)


class SubjectChaptersResponse(BaseModel):
    id: int
    subject_name: str
    chapter_name: str

class LessonPlansResponse(BaseModel):
    id: int
    chapter_id: int
    sub_topic: str
    objectives: str
    teaching_methods: str
    resources: str
    assessments: str

class ImportedLessonPlansResponse(BaseModel):
    id: int
    lesson_plan_id: int
    source_url: str

class YearPlanResponse(BaseModel):
    id: int
    year: str
    planned_chapters: List[int]
    status: str

class WeeklyPlansResponse(BaseModel):
    id: int
    year_plan_id: int
    week_number: int
    planned_lessons: List[int]

class StaffLessonPlansResponse(BaseModel):
    id: int
    lesson_plan_id: int
    staff_id: int

class LessonObservationsResponse(BaseModel):
    id: int
    observer_id: int
    lesson_plan_id: int
    objectives: str
    questions: str

class FeedbackAssessmentsResponse(BaseModel):
    id: int
    observation_id: int
    feedback: str
    assessment: str