from pydantic import BaseModel
from datetime import date
from typing import Optional


class HomeworkAssignmentBase(BaseModel):
    teacherID: int
    subjectID: int
    dueDate: date
    description: Optional[str] = None
    additionalInstructions: Optional[str] = None
    attachments: Optional[str] = None



class HomeworkAssignmentCreate(HomeworkAssignmentBase):
    pass

class HomeworkAssignment(HomeworkAssignmentBase):
    assignmentID: int
class Config:
        from_orm = True
class HomeworkSubmissionBase(BaseModel):
    studentID: int
    assignmentID: int
    submissionDate: date  # Change to match SQLAlchemy model
    status: str  # Change to match SQLAlchemy model
    submittedAttachments: Optional[str]  # Change to match SQLAlchemy model



class HomeworkSubmissionCreate(HomeworkSubmissionBase):
    pass

class HomeworkSubmission(HomeworkSubmissionBase):
    submissionID: int

    class Config:
        from_orm = True  # Ensure orm_mode is inside the BaseModel
        

class GradeBase(BaseModel):
    assignmentID: int
    studentID: int
    submissionID:int
    grade: float  # Change to match SQLAlchemy model
    feedback: str  # Change to match SQLAlchemy model

    class Config:
        from_orm = True

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    gradeID: int

# Pydantic Schemas
class TeacherBase(BaseModel):
    firstName: str
    lastName: str
    email: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    teacherID: int
class Config:
        from_orm = True

class StudentBase(BaseModel):
    firstName: str
    lastName: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    studentID: int

class Config:
        from_orm = True
class SubjectBase(BaseModel):
    subjectName: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    subjectID: int

class Config:
        from_orm = True