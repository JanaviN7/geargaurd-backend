from sqlalchemy.orm import Session
from app import models


def create_team(db: Session, name: str):
    team = models.Team(name=name)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def create_equipment(db: Session, data):
    eq = models.Equipment(**data)
    db.add(eq)
    db.commit()
    db.refresh(eq)
    return eq

def create_request(db: Session, data):
    equipment = db.query(models.Equipment).get(data["equipment_id"])

    request = models.MaintenanceRequest(
        subject=data["subject"],
        type=data["type"],
        equipment_id=data["equipment_id"],
        team_id=equipment.team_id,   # 🔥 AUTO-FILL TEAM
        scheduled_date=data.get("scheduled_date")
    )

    db.add(request)
    db.commit()
    db.refresh(request)
    return request
