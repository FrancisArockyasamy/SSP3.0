# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from . import crud, models, schemas
# from .database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Dependency to get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Create endpoints

# @app.post("/teachers/", response_model=schemas.Teacher)
# def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
#     return crud.create_teacher(db=db, teacher=teacher)

# @app.post("/sms/templates/", response_model=schemas.SMSTemplate)
# def create_sms_template(template: schemas.SMSTemplateCreate, db: Session = Depends(get_db)):
#     return crud.create_sms_template(db=db, template=template)

# @app.post("/sms/messages/", response_model=schemas.SentSMSMessage)
# def create_sent_sms_message(message: schemas.SentSMSMessageCreate, db: Session = Depends(get_db)):
#     return crud.create_sent_sms_message(db=db, message=message)

# @app.post("/delivery/status/", response_model=schemas.DeliveryStatus)
# def create_delivery_status(status: schemas.DeliveryStatusCreate, db: Session = Depends(get_db)):
#     return crud.create_delivery_status(db=db, status=status)

# @app.post("/groups/", response_model=schemas.Group)
# def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
#     return crud.create_group(db=db, group=group)

# @app.post("/group/memberships/", response_model=schemas.GroupMembership)
# def create_group_membership(membership: schemas.GroupMembershipCreate, db: Session = Depends(get_db)):
#     return crud.create_group_membership(db=db, membership=membership)

# # Read endpoints

# @app.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
# def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
#     db_teacher = crud.get_teacher(db=db, teacher_id=teacher_id)
#     if db_teacher is None:
#         raise HTTPException(status_code=404, detail="Teacher not found")
#     return db_teacher

# @app.get("/sms/templates/{template_id}", response_model=schemas.SMSTemplate)
# def read_sms_template(template_id: int, db: Session = Depends(get_db)):
#     db_template = crud.get_sms_template(db=db, template_id=template_id)
#     if db_template is None:
#         raise HTTPException(status_code=404, detail="SMS Template not found")
#     return db_template

# # Additional endpoints for other CRUD operations (update, delete) can be added here
