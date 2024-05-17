from pydantic import BaseModel
from datetime import date
from typing import Optional

# class HomeworkSubmissionBase(BaseModel):
#     student_id: int
#     assignment_id: int
#     submission_date: date
#     status: str
#     submitted_attachments: str

# class HomeworkSubmissionCreate(HomeworkSubmissionBase):
#     pass


class HomeworkAssignmentBase(BaseModel):
    teacher_id: int
    subject_id: int
    due_date: date
    description: str
    additional_instructions: Optional[str]
    attachments: Optional[str]

class HomeworkAssignmentCreate(HomeworkAssignmentBase):
    pass

class HomeworkAssignment(HomeworkAssignmentBase):
    assignment_id: int

    class Config:
        from_orm = True


class HomeworkSubmissionBase(BaseModel):
    student_id: int
    assignment_id: int
    submission_date: date
    status: str
    submitted_attachments: Optional[str]

class HomeworkSubmission(HomeworkSubmissionBase):
    pass

class submission(HomeworkSubmissionBase):
    submission_id: int

    class Config:
        from_orm = True
        


# class HomeworkSubmission(HomeworkSubmissionBase):
#     submission_id: int

#     class Config:
#         orm_mode = True

class GradeBase(BaseModel):
    assignment_id: int
    student_id: int
    grade: float
    feedback: str

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    grade_id: int

    class Config:
        from_orm = True
