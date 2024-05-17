from fastapi import APIRouter , Body , Depends , HTTPException , status
from sqlalchemy.orm import Session
from models import ClassSubject , Class , Subject
import schemas
from db import get_db

app=APIRouter(tags=['Class Wise Subjects'])


@app.post("/classes/{class_id}/subjects")
async def assign_subjects_to_class(class_id: int, subject_ids: list[int], db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    # Check if subjects exist
    existing_subjects = db.query(Subject).filter(Subject.id.in_(subject_ids)).all()
    if len(existing_subjects) != len(subject_ids):
        raise HTTPException(status_code=400, detail="One or more subjects not found")
        
    #Check if subjects already mapped to class
    existing_mappings = db.query(ClassSubject).filter(ClassSubject.class_id==class_id and ClassSubject.subject_id.in_(subject_ids)).all()
    if len(existing_mappings)>0:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT ,detail="One or more subjects are already registered")

    # Create new ClassSubject entries for each assigned subject
    for subject in existing_subjects:
        new_assignment = ClassSubject(class_id=class_id, subject_id=subject.id)
        db.add(new_assignment)

    db.commit()
    return {"message": "Subjects assigned to class successfully"}


@app.get("/classes/{class_id}/subjects")
async def get_subjects_assigned_to_class(class_id: int, db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    assigned_subjects = (
        db.query(Subject)
        .join(ClassSubject, ClassSubject.subject_id == Subject.id)
        .filter(ClassSubject.class_id == class_id)
        .all()
    )
    return assigned_subjects



@app.delete("/classes/{class_id}/subjects")
async def unassign_subjects_from_class(class_id: int, subject_ids: list[int], db: Session = Depends(get_db)):
    class_obj = db.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    # Filter existing assignments for the class and subjects
    assignments_to_delete = (
        db.query(ClassSubject)
        .filter(ClassSubject.class_id == class_id)
        .filter(ClassSubject.subject_id.in_(subject_ids))
        .all()
    )

    if not assignments_to_delete:
        raise HTTPException(status_code=400, detail="No assignments found for these subjects")

    for assignment in assignments_to_delete:
        db.delete(assignment)

    db.commit()
    return {"message": "Subjects unassigned from class successfully"}