from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud, models

router = APIRouter(prefix="/equipment", tags=["Equipment"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_equipment(eq: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    return crud.create_equipment(db, eq.dict())

@router.get("")
@router.get("/")
def list_equipment(db: Session = Depends(get_db)):
    return db.query(models.Equipment).all()
