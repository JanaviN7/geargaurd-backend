from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import requests, equipment, teams

app = FastAPI(
    title="GearGuard – Maintenance Tracker",
    redirect_slashes=True
)

# ✅ CORS FIRST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ THEN ROUTERS
app.include_router(requests.router)
app.include_router(equipment.router)
app.include_router(teams.router)
