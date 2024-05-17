from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    email: EmailStr
    phone_number: str
    address: str

class StudentCreate(StudentBase):
    class_id: int

class StudentUpdate(StudentBase):
    pass

class StudentInDB(StudentBase):
    student_id: int
    class_id: int

    class Config:
        orm_mode = True

class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    grade_value: float

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    grade_id: int

    class Config:
        orm_mode = True

class AttendanceBase(BaseModel):
    student_id: int
    class_id: int
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    attendance_id: int

    class Config:
        orm_mode = True

class HomeworkBase(BaseModel):
    class_id: int
    subject_id: int
    deadline: date
    assignment_details: str
    submission_status: str

class HomeworkCreate(HomeworkBase):
    pass

class Homework(HomeworkBase):
    homework_id: int

    class Config:
        orm_mode = True

class RemarkBase(BaseModel):
    student_id: int
    remarks_details: str
    remark_date: date

class RemarkCreate(RemarkBase):
    pass

class Remark(RemarkBase):
    remark_id: int

    class Config:
        orm_mode = True

class SMSUsageBase(BaseModel):
    student_id: int
    messages_sent: int
    remaining_credits: int

class SMSUsageCreate(SMSUsageBase):
    pass

class SMSUsage(SMSUsageBase):
    sms_usage_id: int

    class Config:
        orm_mode = True

class ProgressCardBase(BaseModel):
    student_id: int
    term: str
    academic_year: str
    grade_id: int

class ProgressCardCreate(ProgressCardBase):
    pass

class ProgressCard(ProgressCardBase):
    progress_card_id: int

    class Config:
        orm_mode = True

class FeePaymentBase(BaseModel):
    student_id: int
    payment_date: date
    amount: float
    payment_method: str
    receipt_url: Optional[str] = None

class FeePaymentCreate(FeePaymentBase):
    pass

class FeePayment(FeePaymentBase):
    payment_id: int

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    class_name: str
    class_teacher_id: Optional[int]

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    class_id: int

    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    teacher_id: int

    class Config:
        orm_mode = True