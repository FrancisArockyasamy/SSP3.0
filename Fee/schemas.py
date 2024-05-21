from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from typing import Optional

class FeePaymentBase(BaseModel):
    student_id: int
    fee_structure_id: int
    payment_date: date
    amount_paid: float
    payment_method: str
    receipt_number: str
    status: str

class FeePaymentCreate(FeePaymentBase):
    pass

class FeePayment(FeePaymentBase):
    id: int

    class Config:
        from_orm = True

class FeeStructureBase(BaseModel):
    class_id: int
    fee_type_id: int
    amount: float

class FeeStructureCreate(FeeStructureBase):
    pass

class FeeStructure(FeeStructureBase):
    id: int

    class Config:
        from_orm = True

class FeeTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class FeeTypeCreate(FeeTypeBase):
    pass

class FeeType(FeeTypeBase):
    id: int

class Config:
        from_orm = True

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    class_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_orm = True

class RefundBase(BaseModel):
    payment_id: int
    refund_date: date
    refund_amount: float
    refund_reason: str

class RefundCreate(RefundBase):
    pass

class Refund(RefundBase):
    id: int

    class Config:
        from_orm = True

class ConcessionBase(BaseModel):
    student_id: int
    concession_type: str
    concession_amount: float
    start_date: date
    end_date: date

class ConcessionCreate(ConcessionBase):
    pass

class Concession(ConcessionBase):
    id: int

class Config:
        from_orm = True


class ClassBase(BaseModel):
    name: str
    description: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int

    class Config:
        from_orm = True