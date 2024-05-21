from pydantic import BaseModel
from datetime import date
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str
    # Add other employee details as needed
    class Config:
        orm_mode = True


class Attendance(BaseModel):
    id: Optional[int]= None
    employee_id: int
    attendance_date: date
    attendance_status: str
    session: str
    # Add other attendance details as needed
    class Config:
        orm_mode = True


class LeaveType(BaseModel):
    id: Optional[int]
    name: str
    description: str
    # Add other leave type details as needed
    class Config:
        orm_mode = True


class LeaveRegister(BaseModel):
    id: Optional[int]
    employee_id: int
    leave_type_id: int
    leave_start_date: date
    leave_end_date: date
    leave_status: str
    # Add other leave register details as needed
    class Config:
        orm_mode = True


class LateAttendance(BaseModel):
    id: Optional[int]
    employee_id: int
    late_date: date
    late_reason: str
    # Add other late attendance details as needed
    class Config:
        orm_mode = True


class OnDutyRegister(BaseModel):
    id: Optional[int]
    employee_id: int
    on_duty_date: date
    on_duty_reason: str
    # Add other on-duty register details as needed
    class Config:
        orm_mode = True


class PermissionRegister(BaseModel):
    id: Optional[int]
    employee_id: int
    permission_date: date
    permission_type: str
    permission_status: str
    # Add other permission register details as needed
    class Config:
        orm_mode = True


class MonthlyAttendance(BaseModel):
    id: Optional[int]
    employee_id: int
    month: int
    year: int
    total_working_hours: float
    total_leave_hours: float
    late_count: int
    # Add other monthly attendance details as needed
    class Config:
        orm_mode = True
