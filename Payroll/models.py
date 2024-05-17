from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class PayrollStructure(Base):
    __tablename__ = "payroll_structures"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    # Add other columns as needed
    group_id = Column(Integer, ForeignKey('payroll_groups.id'))

class SalaryComponent(Base):
    __tablename__ = "salary_components"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    formula = Column(String)
    structure_id = Column(Integer, ForeignKey('payroll_structures.id'))

class PayrollGroup(Base):
    __tablename__ = "payroll_groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    component_id = Column(Integer, ForeignKey('salary_components.id'))
