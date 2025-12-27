from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GearGuard – Maintenance Tracker",
    redirect_slashes=True
)

# ✅ CORS MUST COME FIRST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ THEN routers
app.include_router(requests.router)
app.include_router(equipment.router)
app.include_router(teams.router)
