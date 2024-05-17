from fastapi import APIRouter , Depends , HTTPException , status
from ..db import get_db
from ..models import Class , Staff ,ClassStaff , Subject
from sqlalchemy.orm import Session

app = APIRouter(tags=["Class Wise Staff Allocation"])

@app.post("/classes/{class_id}/subjects/{subject_id}/staff/{staff_id}")
async def assign_staff_to_class(class_id: int, subject_id: int, staff_id: int, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    
    subject_obj = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject_obj:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    staff_obj = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff_obj:
        raise HTTPException(status_code=404, detail="Staff not found")

    existing_mapping = db.query(ClassStaff).filter(ClassStaff.class_id==class_id and ClassStaff.subject_id==subject_id).first()
    if existing_mapping:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT ,detail="The subject is already assigned")
    

    # Create new ClassStaff entries for each assigned staff member
    
    new_assignment = ClassStaff(class_id=class_id, staff_id=staff_id,subject_id=subject_id)
    db.add(new_assignment)

    db.commit()
    return {"message": "Staff members assigned to class successfully"}




@app.get("/classes/{class_id}/subjects/{subject_id}/staff")
async def get_staff_assigned_to_class(class_id: int,subject_id: int, db: Session = Depends(get_db)):
    result = db.query(ClassStaff).filter(ClassStaff.class_id == class_id , ClassStaff.subject_id==subject_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="The mentioned class or subject has not assigned to Staff")

    assigned_staff = (
        db.query(Staff)
        .join(ClassStaff, ClassStaff.staff_id == Staff.id)
        .filter(ClassStaff.subject_id == subject_id)
        .all()
    )
    return assigned_staff



@app.delete("/classes/{class_id}/subjects/{subject_id}/staff/{staff_id}")
async def unassign_staff_from_class(class_id: int, subject_id: int, staff_id: int, db: Session = Depends(get_db)):
    result_obj = db.query(ClassStaff).filter(ClassStaff.class_id == class_id,ClassStaff.subject_id==subject_id,ClassStaff.staff_id==staff_id).first()
    if not result_obj:
        raise HTTPException(status_code=404, detail="Staff not found for the given class and subject")

    # Filter existing assignments for the class and staff members
    # assignments_to_delete = (
    #     db.query(ClassStaff)
    #     .filter(ClassStaff.class_id == class_id)
    #     .filter(ClassStaff.subject_id == subject_id)
    #     .filter(ClassStaff.staff_id == staff_id)
    #     .first()
    # )

   

    db.delete(result_obj)

    db.commit()
    return {"message": "Staff member has been unassigned from class successfully"}