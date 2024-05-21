from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from . import schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker
from .models import Base, FeePayment,FeeStructure,FeeType,Refund,Concession,Student,Class
import stripe
from typing import List

stripe.api_key = "your_stripe_api_key"  # Set your Stripe API key here

app = APIRouter( prefix="/fee",
    tags=["Fee"])

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.post("/fee_payment/")
def create_fee_payment(fee_payment: schemas.FeePaymentCreate, db: Session = Depends(get_db)):
    new_fee_payment = FeePayment(**fee_payment.dict())
    db.add(new_fee_payment)
    db.commit()
    db.refresh(new_fee_payment)
    return new_fee_payment

@app.get("/fee_payment_findById/{fee_payment_id}", response_model=schemas.FeePayment)
def get_fee_payment(fee_payment_id: int, db: Session = Depends(get_db)):
    return db.query(FeePayment).filter(FeePayment.id == fee_payment_id).first()

@app.get("/fee_payments_list", response_model=List[schemas.FeePayment])
def list_fee_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(FeePayment).offset(skip).limit(limit).all()

@app.get("/fee_payments_list_withoutlimit/", response_model=List[schemas.FeePayment])
def fee_payments_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(FeePayment).all()

@app.delete("/fee_payment_delete/{fee_payment_id}", response_model=schemas.FeePayment)
def delete_fee_payment(fee_payment_id: int, db: Session = Depends(get_db)):
    fee_payment = db.query(FeePayment).filter(FeePayment.id == fee_payment_id).first()
    if fee_payment:
        db.delete(fee_payment)
        db.commit()
        return fee_payment
    raise HTTPException(status_code=404, detail="Fee Payment not found")


# Create fee structure
@app.post("/fee_structur/")
def create_fee_structure(fee_structure: schemas.FeeStructureCreate, db: Session = Depends(get_db)):
    new_fee_structure = FeeStructure(**fee_structure.dict())
    db.add(new_fee_structure)
    db.commit()
    db.refresh(new_fee_structure)
    return new_fee_structure
# List fee structures
@app.get("/fee_structures_list/", response_model=List[schemas.FeeStructure])
def list_fee_structures(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(FeeStructure).offset(skip).limit(limit).all()

# List fee structures
@app.get("/fee_structures_list_withoutlimit/", response_model=List[schemas.FeeStructure])
def fee_structures_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(FeeStructure).all()

# Find fee structure by ID
@app.get("/fee_structure_findbyId/{fee_structure_id}", response_model=schemas.FeeStructure)
def find_fee_structure(fee_structure_id: int, db: Session = Depends(get_db)):
    fee_structure = db.query(FeeStructure).filter(FeeStructure.id == fee_structure_id).first()
    if not fee_structure:
        raise HTTPException(status_code=404, detail="Fee Structure not found")
    return fee_structure

# Delete fee structure
@app.delete("/fee_structure_delete/{fee_structure_id}", response_model=schemas.FeeStructure)
def delete_fee_structure(fee_structure_id: int, db: Session = Depends(get_db)):
    fee_structure = db.query(FeeStructure).filter(FeeStructure.id == fee_structure_id).first()
    if not fee_structure:
        raise HTTPException(status_code=404, detail="Fee Structure not found")
    db.delete(fee_structure)
    db.commit()
    return fee_structure

# Create fee type
@app.post("/fee_type/")
def create_fee_type(fee_type: schemas.FeeTypeCreate, db: Session = Depends(get_db)):
    new_fee_type = FeeType(**fee_type.dict())
    db.add(new_fee_type)
    db.commit()
    db.refresh(new_fee_type)
    return new_fee_type
# List fee types
@app.get("/fee_type_list/", response_model=List[schemas.FeeType])
def list_fee_types(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(FeeType).offset(skip).limit(limit).all()

# List fee types
@app.get("/fee_type_list_without_limit/", response_model=List[schemas.FeeType])
def list_fee_types_list_without_limit(db: Session = Depends(get_db)):
    return db.query(FeeType).all()

# Find fee type by ID
@app.get("/fee_type_findById/{fee_type_id}", response_model=schemas.FeeType)
def find_fee_type(fee_type_id: int, db: Session = Depends(get_db)):
    fee_type = db.query(FeeType).filter(FeeType.id == fee_type_id).first()
    if not fee_type:
        raise HTTPException(status_code=404, detail="Fee Type not found")
    return fee_type

# Delete fee type
@app.delete("/fee_type_delete/{fee_type_id}", response_model=schemas.FeeType)
def delete_fee_type(fee_type_id: int, db: Session = Depends(get_db)):
    fee_type = db.query(FeeType).filter(FeeType.id == fee_type_id).first()
    if not fee_type:
        raise HTTPException(status_code=404, detail="Fee Type not found")
    db.delete(fee_type)
    db.commit()
    return fee_type

# Create student
@app.post("/student/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# List students
@app.get("/students_list/", response_model=List[schemas.Student])
def list_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Student).offset(skip).limit(limit).all()
# List students
@app.get("/students_list_withoutlimit/", response_model=List[schemas.Student])
def students_list_withoutlimit( db: Session = Depends(get_db)):
    return db.query(Student).all()

# Find student by ID
@app.get("/student_findById/{student_id}", response_model=schemas.Student)
def find_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Delete student
@app.delete("/student_delete/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return student

# Create refund
@app.post("/refund/")
def create_refund(refund: schemas.RefundCreate, db: Session = Depends(get_db)):
    new_refund = Refund(**refund.dict())
    db.add(new_refund)
    db.commit()
    db.refresh(new_refund)
    return new_refund

@app.get("/refundList")
def refundlist(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
 return db.query(Refund).offset(skip).limit(limit).all()

# Create concession
@app.post("/concession/")
def create_concession(concession: schemas.ConcessionCreate, db: Session = Depends(get_db)):
    new_concession = Concession(**concession.dict())
    db.add(new_concession)
    db.commit()
    db.refresh(new_concession)
    return new_concession


# Create class
@app.post("/class/")
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    new_class = Class(**class_.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

# List classes
@app.get("/class_list/", response_model=List[schemas.Class])
def list_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Class).offset(skip).limit(limit).all()

# List classes
@app.get("/class_list_withoutlimit/", response_model=List[schemas.Class])
def class_list_withoutlimit(db: Session = Depends(get_db)):
    return db.query(Class).all()

# Handle webhook events from Stripe  
# @app.post("/webhook/")
# async def stripe_webhook(request: Request):
#     db = SessionLocal()
#     payload = await request.body()
#     sig_header = request.headers.get('Stripe-Signature')

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, "your_stripe_webhook_secret"
#         )
#     except ValueError as e:
#         # Invalid payload
#         return "Invalid payload", 400
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return "Invalid signature", 400

#     # Handle the event
#     if event['type'] == 'payment_intent.succeeded':
#         payment_intent = event['data']['object']
#         payment = db.query(Payment).filter(Payment.payment_id == payment_intent['id']).first()
#         if payment:
#             payment.status = "succeeded"
#             db.commit()
#     elif event['type'] == 'payment_intent.payment_failed':
#         payment_intent = event['data']['object']
#         payment = db.query(Payment).filter(Payment.payment_id == payment_intent['id']).first()
#         if payment:
#             payment.status = "failed"
#             db.commit()

#     db.close()
#     return "Success"
