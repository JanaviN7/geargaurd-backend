from pydantic import BaseModel
from datetime import date
from typing import Optional

class TeamCreate(BaseModel):
    name: str

class EquipmentCreate(BaseModel):
    name: str
    serial_number: str
    department: str
    location: str
    team_id: int

class RequestCreate(BaseModel):
    subject: str
    type: str
    equipment_id: int
    scheduled_date: Optional[date] = None

class RequestUpdate(BaseModel):
    status: str
    duration_hours: Optional[int] = None
