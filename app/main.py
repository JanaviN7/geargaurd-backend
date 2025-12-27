from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import equipment, requests, teams
from fastapi.middleware.cors import CORSMiddleware

# create tables
models.Base.metadata.create_all(bind=engine)

# CREATE APP FIRST ✅
app = FastAPI(title="GearGuard – Maintenance Tracker", redirect_slashes = True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# root health check
@app.get("/")
def root():
    return {"status": "GearGuard API running"}

# register routers
app.include_router(teams.router)
app.include_router(equipment.router)
app.include_router(requests.router)
