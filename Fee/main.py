from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from . import schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker
from .models import Base, FeePayment
import stripe

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


# Define Payment model here if it's not already defined

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create payment
# @app.post("/payments/")
# def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
#     new_payment = Payment(
#         amount=payment.amount,
#         currency=payment.currency,
#         description=payment.description,
#         status="pending"  
#     )
#     db.add(new_payment)
#     db.commit()
#     return new_payment

@app.post("/payments/")
def FeePaymentCreate(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    new_payment = FeePayment(
        amount=payment.amount,
        currency=payment.currency,
        description=payment.description,
        status="pending"  
    )
    db.add(new_payment)
    db.commit()
    return new_payment

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
