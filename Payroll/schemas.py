from pydantic import BaseModel

class PayrollStructureBase(BaseModel):
    name: str

class SalaryComponentBase(BaseModel):
    name: str
    formula: str
    structure_id: int

class PayrollGroupBase(BaseModel):
    name: str
    employee_id: int
    component_id: int

class PayrollStructure(PayrollStructureBase):
    id: int

    class Config:
        orm_mode = True

class SalaryComponent(SalaryComponentBase):
    id: int

    class Config:
        orm_mode = True

class PayrollGroup(PayrollGroupBase):
    id: int

    class Config:
        orm_mode = True
