# from sqlalchemy.orm import Session
# from . import models, schemas

# # Create operations

# def create_teacher(db: Session, teacher: schemas.TeacherCreate):
#     db_teacher = models.Teacher(**teacher.dict())
#     db.add(db_teacher)
#     db.commit()
#     db.refresh(db_teacher)
#     return db_teacher

# def create_sms_template(db: Session, template: schemas.SMSTemplateCreate):
#     db_template = models.SMSTemplate(**template.dict())
#     db.add(db_template)
#     db.commit()
#     db.refresh(db_template)
#     return db_template

# def create_sent_sms_message(db: Session, message: schemas.SentSMSMessageCreate):
#     db_message = models.SentSMSMessage(**message.dict())
#     db.add(db_message)
#     db.commit()
#     db.refresh(db_message)
#     return db_message

# def create_delivery_status(db: Session, status: schemas.DeliveryStatusCreate):
#     db_status = models.DeliveryStatus(**status.dict())
#     db.add(db_status)
#     db.commit()
#     db.refresh(db_status)
#     return db_status

# def create_group(db: Session, group: schemas.GroupCreate):
#     db_group = models.Group(**group.dict())
#     db.add(db_group)
#     db.commit()
#     db.refresh(db_group)
#     return db_group

# def create_group_membership(db: Session, membership: schemas.GroupMembershipCreate):
#     db_membership = models.GroupMembership(**membership.dict())
#     db.add(db_membership)
#     db.commit()
#     db.refresh(db_membership)
#     return db_membership

# # Read operations

# def get_teacher(db: Session, teacher_id: int):
#     return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

# def get_sms_template(db: Session, template_id: int):
#     return db.query(models.SMSTemplate).filter(models.SMSTemplate.id == template_id).first()

# def get_sent_sms_message(db: Session, message_id: int):
#     return db.query(models.SentSMSMessage).filter(models.SentSMSMessage.id == message_id).first()

# def get_delivery_status(db: Session, delivery_id: int):
#     return db.query(models.DeliveryStatus).filter(models.DeliveryStatus.id == delivery_id).first()

# def get_group(db: Session, group_id: int):
#     return db.query(models.Group).filter(models.Group.id == group_id).first()

# def get_group_membership(db: Session, membership_id: int):
#     return db.query(models.GroupMembership).filter(models.GroupMembership.id == membership_id).first()

# # Update operations

# def update_sms_template(db: Session, template_id: int, updated_template: schemas.SMSTemplateCreate):
#     db_template = db.query(models.SMSTemplate).filter(models.SMSTemplate.id == template_id).first()
#     for key, value in updated_template.dict().items():
#         setattr(db_template, key, value)
#     db.commit()
#     db.refresh(db_template)
#     return db_template

# # Delete operations

# def delete_sms_template(db: Session, template_id: int):
#     db_template = db.query(models.SMSTemplate).filter(models.SMSTemplate.id == template_id).first()
#     db.delete(db_template)
#     db.commit()
#     return db_template
