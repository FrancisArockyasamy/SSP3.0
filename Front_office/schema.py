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
