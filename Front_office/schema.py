from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VisitorBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone_number: Optional[str] = None
    purpose_of_visit: Optional[str] = None
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
class VisitorCreate(VisitorBase):
    pass

class Visitor(VisitorBase):
    visitor_id: int
    
    class Config:
        from_orm = True


class PackageBase(BaseModel):
    sender_name: str
    sender_address: str
    recipient_name: str
    recipient_address: str
    delivery_status: str
    received_at: Optional[datetime]
    delivered_at: Optional[datetime] = None
class PackageCreate(PackageBase):
    pass

class Package(PackageBase):
    package_id: int
   
    
    class Config:
        from_orm = True

class CallBase(BaseModel):
    caller_name: str
    caller_number: str
    recipient_name: str
    recipient_number: str
    call_purpose: str
    call_type:Optional[str]
    call_time:Optional[datetime]
class CallCreate(CallBase):
    pass

class Call(CallBase):
    call_id: int
    
    
    class Config:
        from_orm = True

class GatePassBase(BaseModel):
    visitor_id: int
    staff_member_id: int
    purpose: str
    issued_at: datetime
    valid_until:  Optional[datetime] = None
class GatePassCreate(GatePassBase):
    pass

class GatePass(GatePassBase):
    gate_pass_id: int
    
    class Config:
        from_orm = True

class StaffMemberBase(BaseModel):
    name: str
    department: str
    designation: str

class StaffMemberCreate(StaffMemberBase):
    pass

class StaffMember(StaffMemberBase):
    staff_member_id: int
    
    class Config:
        from_orm = True

class CircularBase(BaseModel):
    title: str
    content: str
    author: str
    date_published: datetime
class CircularCreate(CircularBase):
    pass

class Circular(CircularBase):
    circular_id: int
   
    
    class Config:
        from_orm = True

class ComplaintBase(BaseModel):
    visitor_id: int
    staff_member_id: int
    complaint_type: str
    description: str
    status: str
    date_reported: datetime
    date_resolved: Optional[datetime] = None
class ComplaintCreate(ComplaintBase):
    pass

class Complaint(ComplaintBase):
    complaint_id: int
    
    
    class Config:
        from_orm = True

