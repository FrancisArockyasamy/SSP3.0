from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # You should hash the password here
    db_user = models.User(username=user.username, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Student CRUD operations
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# Mark CRUD operations
def create_mark(db: Session, mark: schemas.MarkBase):
    db_mark = models.Mark(**mark.model_dump())
    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)
    return db_mark

def get_marks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Mark).offset(skip).limit(limit).all()

def get_mark(db: Session, mark_id: int):
    return db.query(models.Mark).filter(models.Mark.mark_id == mark_id).first()

def delete_mark(db: Session, mark_id: int):
    db_mark = db.query(models.Mark).filter(models.Mark.mark_id == mark_id).first()
    if db_mark:
        db.delete(db_mark)
        db.commit()
    return db_mark

def create_examination(db: Session, exam: schemas.ExaminationCreate):
    db_exam = models.Examination(**exam.dict())
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def get_examinations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Examination).offset(skip).limit(limit).all()

def get_examination(db: Session, exam_id: int):
    return db.query(models.Examination).filter(models.Examination.exam_id == exam_id).first()

def update_examination(db: Session, exam_id: int, exam: schemas.ExaminationUpdate):
    db_exam = db.query(models.Examination).filter(models.Examination.exam_id == exam_id).first()
    if db_exam:
        for key, value in exam.dict(exclude_unset=True).items():
            setattr(db_exam, key, value)
        db.commit()
        db.refresh(db_exam)
    return db_exam

def delete_examination(db: Session, exam_id: int):
    db_exam = db.query(models.Examination).filter(models.Examination.exam_id == exam_id).first()
    if db_exam:
        db.delete(db_exam)
        db.commit()
    return db_exam