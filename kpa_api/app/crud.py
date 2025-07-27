from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas

# ---------------- Wheel Spec CRUD ----------------
def create_wheel_spec(db: Session, spec: schemas.WheelSpecCreate):
    existing_spec = db.query(models.WheelSpec).filter(models.WheelSpec.form_number == spec.formNumber).first()
    if existing_spec:
        raise HTTPException(status_code=400, detail=f"Form number {spec.formNumber} already exists.")

    db_spec = models.WheelSpec(
        form_number=spec.formNumber,
        submitted_by=spec.submittedBy,
        submitted_date=spec.submittedDate,
        fields=spec.fields
    )
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)

    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": db_spec.form_number,
            "submittedBy": db_spec.submitted_by,
            "submittedDate": db_spec.submitted_date,
            "status": "Saved"
        }
    }

def get_wheel_specs(db: Session, formNumber: str = None):
    query = db.query(models.WheelSpec)
    if formNumber:
        query = query.filter(models.WheelSpec.form_number == formNumber)
    results = query.all()

    data = []
    for r in results:
        data.append({
            "formNumber": r.form_number,
            "submittedBy": r.submitted_by,
            "submittedDate": r.submitted_date,
            "fields": r.fields
        })

    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": data
    }


# ---------------- Bogie Checksheet CRUD ----------------
def create_bogie_checksheet(db: Session, data: schemas.BogieChecksheetCreate):
    existing = db.query(models.BogieChecksheet).filter(models.BogieChecksheet.form_number == data.formNumber).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Form number {data.formNumber} already exists.")

    db_entry = models.BogieChecksheet(
        form_number=data.formNumber,
        inspection_by=data.inspectionBy,
        inspection_date=data.inspectionDate,
        bogie_details=data.bogieDetails,
        bogie_checksheet=data.bogieChecksheet,
        bmbc_checksheet=data.bmbcChecksheet
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    return {
        "success": True,
        "message": "Bogie checksheet submitted successfully.",
        "data": {
            "formNumber": db_entry.form_number,
            "inspectionBy": db_entry.inspection_by,
            "inspectionDate": db_entry.inspection_date,
            "status": "Saved"
        }
    }
