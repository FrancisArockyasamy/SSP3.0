from sqlalchemy import Column, Integer, String, Date, Float
from .database import Base
from pydantic import BaseModel
from typing import Optional

# from models import Attendance


# Define your SQLAlchemy models here

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Add other columns for employee details as needed


class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    attendance_date = Column(Date)
    attendance_status = Column(String)
    session = Column(String)
    # Add other columns for attendance details as needed
        
    class Config:
            orm_mode = True


class LeaveType(Base):
    __tablename__ = "leave_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    # Add other columns for leave type details as needed


class LeaveRegister(Base):
    __tablename__ = "leave_registers"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    leave_type_id = Column(Integer, index=True)
    leave_start_date = Column(Date)
    leave_end_date = Column(Date)
    leave_status = Column(String)
    # Add other columns for leave register details as needed


class LateAttendance(Base):
    __tablename__ = "late_attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    late_date = Column(Date)
    late_reason = Column(String)
    # Add other columns for late attendance details as needed


class OnDutyRegister(Base):
    __tablename__ = "on_duty_registers"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    on_duty_date = Column(Date)
    on_duty_reason = Column(String)
    # Add other columns for on-duty register details as needed


class PermissionRegister(Base):
    __tablename__ = "permission_registers"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    permission_date = Column(Date)
    permission_type = Column(String)
    permission_status = Column(String)
    # Add other columns for permission register details as needed


class MonthlyAttendanceReport(Base):
    __tablename__ = "monthly_attendance_reports"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, index=True)
    month = Column(Integer)
    year = Column(Integer)
    total_working_hours = Column(Float)
    total_leave_hours = Column(Float)
    late_count = Column(Integer)
    # Add other columns for monthly attendance report details as needed
    
    class Config:
            orm_mode = True