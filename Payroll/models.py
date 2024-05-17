from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from .database import Base

class PayrollStructure(Base):
    __tablename__ = "tbl_payroll_structures"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class Employee(Base):
    __tablename__ = "tbl_employees"
    id = Column(Integer, primary_key=True, index=True)
    # Add other columns as needed
    group_id = Column(Integer, ForeignKey('tbl_payroll_groups.id'))

class SalaryComponent(Base):
    __tablename__ = "tbl_salary_components"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    formula = Column(String)
    structure_id = Column(Integer, ForeignKey('tbl_payroll_structures.id'))

class PayrollGroup(Base):
    __tablename__ = "tbl_payroll_groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    employee_id = Column(Integer, ForeignKey('tbl_employees.id'))
    component_id = Column(Integer, ForeignKey('tbl_salary_components.id'))
