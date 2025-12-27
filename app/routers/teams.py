from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, models

router = APIRouter(prefix="/teams", tags=["Teams"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    obj = models.Team(name=team.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/")
def list_teams(db: Session = Depends(get_db)):
    return db.query(models.Team).all()
