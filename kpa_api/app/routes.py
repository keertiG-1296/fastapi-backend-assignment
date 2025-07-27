from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()


@router.post("/api/forms/wheel-specifications", response_model=schemas.WheelSpecResponse, status_code=201)
def create_wheel_spec(spec: schemas.WheelSpecCreate, db: Session = Depends(database.get_db)):
    return crud.create_wheel_spec(db, spec)

@router.get("/api/forms/wheel-specifications")
def get_wheel_specs(formNumber: str = Query(None), db: Session = Depends(database.get_db)):
    return crud.get_wheel_specs(db, formNumber)

@router.post("/api/forms/bogie-checksheet", response_model=schemas.BogieChecksheetResponse, status_code=201)
def create_bogie_checksheet(data: schemas.BogieChecksheetCreate, db: Session = Depends(database.get_db)):
    return crud.create_bogie_checksheet(db, data)
