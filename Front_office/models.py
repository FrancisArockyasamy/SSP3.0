from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

Base = declarative_base()

class Visitor(Base):
    __tablename__ = 'tbl_visitors'
    
    visitor_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    phone_number = Column(String(255))
    purpose_of_visit = Column(String(255))
    check_in_time = Column(DateTime,nullable=True)
    check_out_time = Column(DateTime,nullable=True)

class Package(Base):
    __tablename__ = 'tbl_packages'
    
    package_id = Column(Integer, primary_key=True)
    sender_name = Column(String(255))
    sender_address = Column(String(255))
    recipient_name = Column(String(255))
    recipient_address = Column(String(255))
    delivery_status = Column(String(255))
    received_at = Column(DateTime,nullable=True)
    delivered_at = Column(DateTime,nullable=True)

class Call(Base):
    __tablename__ = 'tbl_calls'
    
    call_id = Column(Integer, primary_key=True)
    caller_name = Column(String(255))
    caller_number = Column(String(255))
    recipient_name = Column(String(255))
    recipient_number = Column(String(255))
    call_purpose = Column(String(255))
    call_type = Column(String(255),nullable=True)
    call_time = Column(DateTime,nullable=True)

class GatePass(Base):
    __tablename__ = 'tbl_gate_passes'
    
    gate_pass_id = Column(Integer, primary_key=True)
    visitor_id = Column(Integer, ForeignKey('tbl_visitors.visitor_id'))
    staff_member_id = Column(Integer, ForeignKey('tbl_staff_members.staff_member_id'))
    purpose = Column(String(255))
    issued_at = Column(DateTime,nullable=True)
    valid_until = Column(DateTime,nullable=True)

class StaffMember(Base):
    __tablename__ = 'tbl_staff_members'
    
    staff_member_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    department = Column(String(255))
    designation = Column(String(255))
    
    gate_passes = relationship("GatePass")

class Circular(Base):
    __tablename__ = 'tbl_circulars'
    
    circular_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(255))
    author = Column(String(255))
    date_published = Column(DateTime,nullable=True)

class Complaint(Base):
    __tablename__ = 'tbl_complaints'
    
    complaint_id = Column(Integer, primary_key=True)
    visitor_id = Column(Integer, ForeignKey('tbl_visitors.visitor_id'))
    staff_member_id = Column(Integer, ForeignKey('tbl_staff_members.staff_member_id'))
    complaint_type = Column(String(255))
    description = Column(String(255))
    status = Column(String(255))
    date_reported = Column(DateTime,nullable=True)
    date_resolved = Column(DateTime,nullable=True)

Base.metadata.create_all(bind= engine)