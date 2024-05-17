from fastapi import FastAPI, HTTPException, Depends, APIRouter
from .database import SessionLocal, engine
from .models import Base, SMS_Templates, Attendance, Timetable, Exam, FeeReminder, Remarks, PTMNotification, LeftStudents, Alumni
from .schemas import SMS_TemplatesCreate,  AttendanceCreate, TimetableCreate, ExamCreate, FeeReminderCreate, RemarksCreate, PTMNotificationCreate, LeftStudentsCreate, AlumniCreate
from sqlalchemy.orm import Session

app = APIRouter(
    prefix="/communication",
    tags=["Communication"]
)

Base.metadata.create_all(bind=engine)

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_sms_template/")
async def create_sms_template(template: SMS_TemplatesCreate, db: Session = Depends(get_db)):
    db_template = SMS_Templates(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return template

@app.get("/get_sms_template/{template_id}")
async def get_sms_template(template_id: int, db: Session = Depends(get_db)):
    template = db.query(SMS_Templates).filter(SMS_Templates.template_id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

# Create Attendance record
@app.post("/create_attendance/")
async def create_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    db_attendance = Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# Get Attendance record by ID
@app.get("/get_attendance/{attendance_id}")
async def get_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance


# Create Timetable entry
@app.post("/create_timetable/")
async def create_timetable(timetable: TimetableCreate, db: Session = Depends(get_db)):
    db_timetable = Timetable(**timetable.dict())
    db.add(db_timetable)
    db.commit()
    db.refresh(db_timetable)
    return db_timetable

# Get Timetable entry by ID
@app.get("/get_timetable/{timetable_id}")
async def get_timetable(timetable_id: int, db: Session = Depends(get_db)):
    timetable = db.query(Timetable).filter(Timetable.timetable_id == timetable_id).first()
    if not timetable:
        raise HTTPException(status_code=404, detail="Timetable entry not found")
    return timetable

# Create Exam entry
@app.post("/create_exam/")
async def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    db_exam = Exam(**exam.dict())
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

# Get Exam entry by ID
@app.get("/get_exam/{exam_id}")
async def get_exam(exam_id: int, db: Session = Depends(get_db)):
    exam = db.query(Exam).filter(Exam.exam_id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Exam entry not found")
    return exam

# Create Fee Reminder
@app.post("/create_fee_reminder/")
async def create_fee_reminder(fee_reminder: FeeReminderCreate, db: Session = Depends(get_db)):
    db_fee_reminder = FeeReminder(**fee_reminder.dict())
    db.add(db_fee_reminder)
    db.commit()
    db.refresh(db_fee_reminder)
    return db_fee_reminder

# Get Fee Reminder by ID
@app.get("/get_fee_reminder/{reminder_id}")
async def get_fee_reminder(reminder_id: int, db: Session = Depends(get_db)):
    fee_reminder = db.query(FeeReminder).filter(FeeReminder.reminder_id == reminder_id).first()
    if not fee_reminder:
        raise HTTPException(status_code=404, detail="Fee Reminder not found")
    return fee_reminder

# Create Remarks
@app.post("/create_remarks/")
async def create_remarks(remarks: RemarksCreate, db: Session = Depends(get_db)):
    db_remarks = Remarks(**remarks.dict())
    db.add(db_remarks)
    db.commit()
    db.refresh(db_remarks)
    return db_remarks

# Get Remarks by ID
@app.get("/get_remarks/{remark_id}")
async def get_remarks(remark_id: int, db: Session = Depends(get_db)):
    remarks = db.query(Remarks).filter(Remarks.remark_id == remark_id).first()
    if not remarks:
        raise HTTPException(status_code=404, detail="Remarks not found")
    return remarks

# Create PTM Notification
@app.post("/create_ptm_notification/")
async def create_ptm_notification(ptm_notification: PTMNotificationCreate, db: Session = Depends(get_db)):
    db_ptm_notification = PTMNotification(**ptm_notification.dict())
    db.add(db_ptm_notification)
    db.commit()
    db.refresh(db_ptm_notification)
    return db_ptm_notification

# Get PTM Notification by ID
@app.get("/get_ptm_notification/{ptm_id}")
async def get_ptm_notification(ptm_id: int, db: Session = Depends(get_db)):
    ptm_notification = db.query(PTMNotification).filter(PTMNotification.ptm_id == ptm_id).first()
    if not ptm_notification:
        raise HTTPException(status_code=404, detail="PTM Notification not found")
    return ptm_notification

# Create Left Students
@app.post("/create_left_students/")
async def create_left_students(left_students: LeftStudentsCreate, db: Session = Depends(get_db)):
    db_left_students = LeftStudents(**left_students.dict())
    db.add(db_left_students)
    db.commit()
    db.refresh(db_left_students)
    return db_left_students

# Get Left Students by ID
@app.get("/get_left_students/{left_id}")
async def get_left_students(left_id: int, db: Session = Depends(get_db)):
    left_students = db.query(LeftStudents).filter(LeftStudents.left_id == left_id).first()
    if not left_students:
        raise HTTPException(status_code=404, detail="Left Students not found")
    return left_students

# Create Alumni
@app.post("/create_alumni/")
async def create_alumni(alumni: AlumniCreate, db: Session = Depends(get_db)):
    db_alumni = Alumni(**alumni.dict())
    db.add(db_alumni)
    db.commit()
    db.refresh(db_alumni)
    return db_alumni

# Get Alumni by ID
@app.get("/get_alumni/{alumni_id}")
async def get_alumni(alumni_id: int, db: Session = Depends(get_db)):
    alumni = db.query(Alumni).filter(Alumni.alumni_id == alumni_id).first()
    if not alumni:
        raise HTTPException(status_code=404, detail="Alumni not found")
    return alumni
