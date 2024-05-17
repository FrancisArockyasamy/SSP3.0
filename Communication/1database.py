# from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship
# from datetime import datetime

# # DATABASE_URL = "sqlite:///./school_communication.db"
# # engine = create_engine(DATABASE_URL)
# DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/fastApipy"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class Teacher(Base):
#     __tablename__ = "teachers"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)

# class SMSTemplate(Base):
#     __tablename__ = "sms_templates"
#     id = Column(Integer, primary_key=True, index=True)
#     template_name = Column(String, index=True)
#     message_content = Column(String)
#     category = Column(String, index=True)
#     created_by = Column(Integer, ForeignKey('teachers.id'))
#     created_at = Column(DateTime, default=datetime.now)
#     last_updated_by = Column(Integer, ForeignKey('teachers.id'))
#     last_updated_at = Column(DateTime, default=datetime.now)

# class SentSMSMessage(Base):
#     __tablename__ = "sent_sms_messages"
#     id = Column(Integer, primary_key=True, index=True)
#     sender_id = Column(Integer, ForeignKey('teachers.id'))
#     recipient_type = Column(String, index=True)
#     recipient_id = Column(Integer, index=True)
#     template_id = Column(Integer, ForeignKey('sms_templates.id'))
#     message_content = Column(String)
#     timestamp = Column(DateTime, default=datetime.now)

# class DeliveryStatus(Base):
#     __tablename__ = "delivery_status"
#     id = Column(Integer, primary_key=True, index=True)
#     message_id = Column(Integer, ForeignKey('sent_sms_messages.id'))
#     recipient_type = Column(String, index=True)
#     recipient_id = Column(Integer, index=True)
#     delivery_status = Column(String, index=True)
#     delivery_time = Column(DateTime, default=datetime.now)

# class Group(Base):
#     __tablename__ = "groups"
#     id = Column(Integer, primary_key=True, index=True)
#     group_name = Column(String, index=True)
#     group_type = Column(String, index=True)
#     created_by = Column(Integer, ForeignKey('teachers.id'))
#     created_at = Column(DateTime, default=datetime.now)
#     last_updated_by = Column(Integer, ForeignKey('teachers.id'))
#     last_updated_at = Column(DateTime, default=datetime.now)

# class GroupMembership(Base):
#     __tablename__ = "group_membership"
#     id = Column(Integer, primary_key=True, index=True)
#     group_id = Column(Integer, ForeignKey('groups.id'))
#     member_type = Column(String, index=True)
#     member_id = Column(Integer, index=True)

# Base.metadata.create_all(bind=engine)
