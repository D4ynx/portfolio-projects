from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.database import engine, Base
from api.auth import router as auth_router
from api.quest import router as quests_router

## INITIATION
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message": "Campus Quest API is running "}

## FOR LOGIN / AUTHENTICATION -- auth.py
app.include_router(auth_router, prefix="/auth")
    
## FOR QUESTS / quest.py
app.include_router(quests_router, prefix="/quests")