from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from typing import Optional
class FeeTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class FeeTypeCreate(FeeTypeBase):
    pass

class FeeType(FeeTypeBase):
    id: int

    class Config:
         from_orm = True

class ClassBase(BaseModel):
    name: str
    description: Optional[str] = None

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    fee_structures: List['FeeStructure'] = []

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
    class_: Class
    fee_type: FeeType

    class Config:
        from_orm = True
# Define schemas for other tables similarly


class PaymentBase(BaseModel):
    amount: float
    currency:Optional[str] = None
    description: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
         from_orm = True



         #new Added

class FeePaymentBase(BaseModel):
    student_id: int
    fee_structure_id: int
    payment_date: date
    amount_paid: float
    payment_method: Optional[str] = None
    receipt_number: Optional[str] = None
    status: Optional[str] = None

class FeePaymentCreate(FeePaymentBase):
    pass

class FeePayment(FeePaymentBase):
    id: int

    class Config:
         from_orm= True