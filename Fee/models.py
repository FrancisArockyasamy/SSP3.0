from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base,engine


class FeePayment(Base):
    __tablename__ = "tbl_fee_payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.id"))
    fee_structure_id = Column(Integer, ForeignKey("tbl_fee_structures.id"))
    payment_date = Column(Date)
    amount_paid = Column(Float)
    payment_method = Column(String(255))
    receipt_number = Column(String(255))
    status = Column(String(255))

    student = relationship("Student", back_populates="fee_payments")
    fee_structure = relationship("FeeStructure", back_populates="fee_payments")
    refund = relationship("Refund", back_populates="fee_payment")  # Add this line


class FeeStructure(Base):
    __tablename__ = "tbl_fee_structures"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("tbl_classes.id"))
    fee_type_id = Column(Integer, ForeignKey("tbl_fee_types.id"))
    amount = Column(Float)

    fee_type = relationship("FeeType", back_populates="fee_structures")
    class_ = relationship("Class", back_populates="fee_structures")
    fee_payments = relationship("FeePayment", back_populates="fee_structure")  # Add this line


class FeeType(Base):
    __tablename__ = "tbl_fee_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255))

    fee_structures = relationship("FeeStructure", back_populates="fee_type")


class Student(Base):
    __tablename__ = "tbl_students" 

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    class_id = Column(Integer, ForeignKey("tbl_classes.id"))

    class_ = relationship("Class", back_populates="students")
    fee_payments = relationship("FeePayment", back_populates="student")
    concessions = relationship("Concession", back_populates="student")  # Add this line


class Refund(Base):
    __tablename__ = "tbl_refunds"

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(Integer, ForeignKey("tbl_fee_payments.id"))
    refund_date = Column(Date)
    refund_amount = Column(Float)
    refund_reason = Column(String(255))

    fee_payment = relationship("FeePayment", back_populates="refund")


class Concession(Base):
    __tablename__ = "tbl_concessions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("tbl_students.id"))
    concession_type = Column(String(255))
    concession_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)

    student = relationship("Student", back_populates="concessions")


class Class(Base): 
    __tablename__ = "tbl_classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    students = relationship("Student", back_populates="class_")
    fee_structures = relationship("FeeStructure", back_populates="class_")


Base.metadata.create_all(bind=engine)
