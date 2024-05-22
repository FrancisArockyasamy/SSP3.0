from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, schema
from typing import List
app = APIRouter(
     prefix="/front_office",
    tags=["Front_office"]
)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/visitors/", response_model=schema.Visitor)
def create_visitor(visitor: schema.VisitorCreate, db: Session = Depends(get_db)):
    db_visitor = models.Visitor(**visitor.dict())
    db.add(db_visitor)
    db.commit()
    db.refresh(db_visitor)
    return db_visitor

@app.get("/visitorList",response_model=List[schema.Visitor])
def visitor_Listget(db:Session=Depends(get_db)):
    return db.query(models.Visitor).all()

@app.get("/visitors_find/{visitor_id}", response_model=schema.Visitor)
def get_visitor(visitor_id: int, db: Session = Depends(get_db)):
    db_visitor = db.query(models.Visitor).filter(models.Visitor.visitor_id == visitor_id).first()
    if db_visitor is None:
        raise HTTPException(status_code=404, detail="Visitor not found")
    return db_visitor
@app.post("/packages/", response_model=schema.Package)
def create_package(package: schema.PackageCreate, db: Session = Depends(get_db)):
    db_package = models.Package(**package.dict())
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package

@app.get("/packagesList",response_model=List[schema.Package])
def packagesrList(db:Session=Depends(get_db)):
    return db.query(models.Package).all()



@app.get("/packages_find/{package_id}", response_model=schema.Package)
def get_package(package_id: int, db: Session = Depends(get_db)):
    db_package = db.query(models.Package).filter(models.Package.package_id == package_id).first()
    if db_package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return db_package

@app.post("/calls/", response_model=schema.Call)
def create_call(call: schema.CallCreate, db: Session = Depends(get_db)):
    db_call = models.Call(**call.dict())
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call

@app.get("/callsList",response_model=List[schema.Call])
def callsList(db:Session=Depends(get_db)):
    return db.query(models.Call).all()

@app.get("/calls_find/{call_id}", response_model=schema.Call)
def get_call(call_id: int, db: Session = Depends(get_db)):
    db_call = db.query(models.Call).filter(models.Call.call_id == call_id).first()
    if db_call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call

@app.post("/gate_passes/", response_model=schema.GatePass)
def create_gate_pass(gate_pass: schema.GatePassCreate, db: Session = Depends(get_db)):
    db_gate_pass = models.GatePass(**gate_pass.dict())
    db.add(db_gate_pass)
    db.commit()
    db.refresh(db_gate_pass)
    return db_gate_pass

@app.get("/gatePassList",response_model=List[schema.GatePass])
def gatePassList(db:Session=Depends(get_db)):
    return db.query(models.GatePass).all()

@app.get("/gate_passes/{gate_pass_id}", response_model=schema.GatePass)
def get_gate_pass(gate_pass_id: int, db: Session = Depends(get_db)):
    db_gate_pass = db.query(models.GatePass).filter(models.GatePass.gate_pass_id == gate_pass_id).first()
    if db_gate_pass is None:
        raise HTTPException(status_code=404, detail="Gate pass not found")
    return db_gate_pass

@app.post("/staff_members/", response_model=schema.StaffMember)
def create_staff_member(staff_member: schema.StaffMemberCreate, db: Session = Depends(get_db)):
    db_staff_member = models.StaffMember(**staff_member.dict())
    db.add(db_staff_member)
    db.commit()
    db.refresh(db_staff_member)
    return db_staff_member


@app.get("/staff_memberList",response_model=List[schema.StaffMember])
def staff_memberList(db:Session=Depends(get_db)):
    return db.query(models.StaffMember).all()

@app.get("/staff_members_find/{staff_member_id}", response_model=schema.StaffMember)
def get_staff_member(staff_member_id: int, db: Session = Depends(get_db)):
    db_staff_member = db.query(models.StaffMember).filter(models.StaffMember.staff_member_id == staff_member_id).first()
    if db_staff_member is None:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return db_staff_member

@app.post("/circulars/", response_model=schema.Circular)
def create_circular(circular: schema.CircularCreate, db: Session = Depends(get_db)):
    db_circular = models.Circular(**circular.dict())
    db.add(db_circular)
    db.commit()
    db.refresh(db_circular)
    return db_circular

@app.get("/CircularList",response_model=List[schema.Circular])
def circularList(db:Session=Depends(get_db)):
    return db.query(models.Circular).all()

@app.get("/circulars/{circular_id}", response_model=schema.Circular)
def get_circular(circular_id: int, db: Session = Depends(get_db)):
    db_circular = db.query(models.Circular).filter(models.Circular.circular_id == circular_id).first()
    if db_circular is None:
        raise HTTPException(status_code=404, detail="Circular not found")
    return db_circular

@app.post("/complaints/", response_model=schema.Complaint)
def create_complaint(complaint: schema.ComplaintCreate, db: Session = Depends(get_db)):
    db_complaint = models.Complaint(**complaint.dict())
    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)
    return db_complaint

@app.get("/complaintList",response_model=List[schema.Complaint])
def complaintList(db:Session=Depends(get_db)):
    return db.query(models.Complaint).all()

@app.get("/complaints/{complaint_id}", response_model=schema.Complaint)
def get_complaint(complaint_id: int, db: Session = Depends(get_db)):
    db_complaint = db.query(models.Complaint).filter(models.Complaint.complaint_id == complaint_id).first()
    if db_complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return db_complaint