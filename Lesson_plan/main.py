# main.py

from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .models import *
from .schemas import *
from .database import *
from datetime import datetime

app= APIRouter(
    prefix="/lessonPlan",
    tags=["Lesson Plan"]
)
# Dependency for getting database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# 1. Subject Chapters
@app.post("/subject_chapters/", response_model=SubjectChaptersResponse)
def create_subject_chapter(subject_chapter: SubjectChapterCreate, db: Session = Depends(get_db)):
    db_subject_chapter = SubjectChapters(**subject_chapter.dict())
    db.add(db_subject_chapter)
    db.commit()
    db.refresh(db_subject_chapter)
    return db_subject_chapter

# 2. Lesson Plans
@app.post("/lesson_plans/", response_model=LessonPlansResponse)
def create_lesson_plan(lesson_plan: LessonPlanCreate, db: Session = Depends(get_db)):
    db_lesson_plan = LessonPlans(**lesson_plan.dict())
    db.add(db_lesson_plan)
    db.commit()
    db.refresh(db_lesson_plan)
    return db_lesson_plan

# 3. Imported Lesson Plans
@app.post("/imported_lesson_plans/", response_model=ImportedLessonPlansResponse)
def create_imported_lesson_plan(imported_lesson_plan: ImportedLessonPlanCreate, db: Session = Depends(get_db)):
    db_imported_lesson_plan = ImportedLessonPlans(**imported_lesson_plan.dict())
    db.add(db_imported_lesson_plan)
    db.commit()
    db.refresh(db_imported_lesson_plan)
    return db_imported_lesson_plan

# 4. Year Plan
@app.post("/year_plans/", response_model=YearPlanResponse)
def create_year_plan(year_plan: YearPlanCreate, db: Session = Depends(get_db)):
    # year_plan.year =datetime.strptime(year_plan["year"], "%Y-%m-%d").date()

    db_year_plan = YearPlan(**year_plan.dict())
    db.add(db_year_plan)
    db.commit()
    db.refresh(db_year_plan)
    return db_year_plan

# 5. Weekly Plans
@app.post("/weekly_plans/", response_model=WeeklyPlansResponse)
def create_weekly_plan(weekly_plan: WeeklyPlanCreate, db: Session = Depends(get_db)):
    db_weekly_plan = WeeklyPlans(**weekly_plan.dict())
    db.add(db_weekly_plan)
    db.commit()
    db.refresh(db_weekly_plan)
    return db_weekly_plan

# 6. Staff Lesson Plans
@app.post("/staff_lesson_plans/", response_model=StaffLessonPlansResponse)
def create_staff_lesson_plan(staff_lesson_plan: StaffLessonPlanCreate, db: Session = Depends(get_db)):
    db_staff_lesson_plan = StaffLessonPlans(**staff_lesson_plan.dict())
    db.add(db_staff_lesson_plan)
    db.commit()
    db.refresh(db_staff_lesson_plan)
    return db_staff_lesson_plan

# 7. Lesson Observations
@app.post("/lesson_observations/", response_model=LessonObservationsResponse)
def create_lesson_observation(lesson_observation: LessonObservationCreate, db: Session = Depends(get_db)):
    db_lesson_observation = LessonObservations(**lesson_observation.dict())
    db.add(db_lesson_observation)
    db.commit()
    db.refresh(db_lesson_observation)
    return db_lesson_observation

# 8. Feedback and Assessments
@app.post("/feedback_assessments/", response_model=FeedbackAssessmentsResponse)
def create_feedback_assessment(feedback_assessment: FeedbackAssessmentCreate, db: Session = Depends(get_db)):
    db_feedback_assessment = FeedbackAssessments(**feedback_assessment.dict())
    db.add(db_feedback_assessment)
    db.commit()
    db.refresh(db_feedback_assessment)
    return db_feedback_assessment