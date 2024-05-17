from pydantic import BaseModel
from typing import List

class SMS_TemplatesBase(BaseModel):
    template_name: str
    template_content: str
    template_type: str

class SMS_TemplatesCreate(SMS_TemplatesBase):
    pass

class AttendanceBase(BaseModel):
    date: str
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class TimetableBase(BaseModel):
    day: str
    time: str
    subject: str

class TimetableCreate(TimetableBase):
    pass

class ExamBase(BaseModel):
    subject: str
    portion: str
    result: str

class ExamCreate(ExamBase):
    pass

class FeeReminderBase(BaseModel):
    amount: int
    due_date: str

class FeeReminderCreate(FeeReminderBase):
    pass

class RemarksBase(BaseModel):
    subject: str
    remark_content: str

class RemarksCreate(RemarksBase):
    pass

class PTMNotificationBase(BaseModel):
    date: str
    notification_content: str

class PTMNotificationCreate(PTMNotificationBase):
    pass

class LeftStudentsBase(BaseModel):
    reason: str

class LeftStudentsCreate(LeftStudentsBase):
    pass

class AlumniBase(BaseModel):
    graduation_year: int
    last_contact_date: str

class AlumniCreate(AlumniBase):
    pass