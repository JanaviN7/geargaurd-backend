from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud, models
from app.models import RequestStatus




router = APIRouter(prefix="/requests", tags=["Requests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_request(req: schemas.RequestCreate, db: Session = Depends(get_db)):
    return crud.create_request(db, req.dict())

@router.get("/")
def list_requests(db: Session = Depends(get_db)):
    return db.query(models.MaintenanceRequest).all()


@router.put("/{request_id}")
def update_request(request_id: int, data: schemas.RequestUpdate, db: Session = Depends(get_db)):
    req = db.query(models.MaintenanceRequest).get(request_id)

    if not req:
        return {"error": "Request not found"}

    req.status = data.status
    req.duration_hours = data.duration_hours

    db.commit()
    db.refresh(req)
    return req
@router.get("")
@router.get("")
def list_requests_no_slash(db: Session = Depends(get_db)):
    return db.query(models.MaintenanceRequest).all()
