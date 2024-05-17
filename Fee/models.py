from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base,engine


class FeeStructure(Base):
    __tablename__ = "fee_structures"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    fee_type_id = Column(Integer, ForeignKey("fee_types.id"))
    amount = Column(Float)

    fee_type = relationship("FeeType", back_populates="fee_structures")
    class_ = relationship("Class", back_populates="fee_structures")

class FeeType(Base):
    __tablename__ = "fee_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255))

    fee_structures = relationship("FeeStructure", back_populates="fee_type")


class Student(Base):
    __tablename__ = "students" 

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    class_id = Column(Integer, ForeignKey("classes.id"))

    class_ = relationship("Class", back_populates="students")
    fee_payments = relationship("FeePayment", back_populates="student")

class FeePayment(Base):
    __tablename__ = "fee_payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    fee_structure_id = Column(Integer, ForeignKey("fee_structures.id"))
    payment_date = Column(Date)
    amount_paid = Column(Float)
    payment_method = Column(String(255))
    receipt_number = Column(String(255))
    status = Column(String(255))

    student = relationship("Student", back_populates="fee_payments")
    fee_structure = relationship("FeeStructure", back_populates="fee_payments")

class Refund(Base):
    __tablename__ = "refunds"

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(Integer, ForeignKey("fee_payments.id"))
    refund_date = Column(Date)
    refund_amount = Column(Float)
    refund_reason = Column(String(255))

    fee_payment = relationship("FeePayment", back_populates="refund")

class Concession(Base):
    __tablename__ = "concessions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    concession_type = Column(String(255))
    concession_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)

    student = relationship("Student", back_populates="concessions")

Base.metadata.create_all(bind= engine)

# class Payment(Base):
#     __tablename__ = 'payments'

#     id = Column(Integer, primary_key=True, index=True)
#     amount = Column(Float)
#     currency = Column(String(255) )
#     description = Column(String(255))
#     status = Column(String(255))