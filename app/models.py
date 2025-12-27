from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class RequestStatus(str, enum.Enum):
    new = "New"
    in_progress = "In Progress"
    repaired = "Repaired"
    scrap = "Scrap"

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Equipment(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    serial_number = Column(String)
    department = Column(String)
    location = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team")

class MaintenanceRequest(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    type = Column(String)
    status = Column(String, default="New")   # ✅ STRING
    scheduled_date = Column(Date, nullable=True)
    duration_hours = Column(Integer, nullable=True)

    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
