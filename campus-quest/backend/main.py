from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from db.database import engine, Base, get_db
from models.user import User 
from models.quest import Quest
from api.auth import hash_password, verify_password, create_token, verify_token
from sqlalchemy.orm import Session
from datetime import date

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

## CLASSES for AUTH
class RegisterRequest(BaseModel):
    username : str
    name : str
    email : str
    password : str
    
class LoginRequest(BaseModel):
    email : str
    password : str

class QuestRequest(BaseModel):
    quest_name : str
    quest_description: str
    xp_earned : int
    quest_deadline : date
    
## INITIATION
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

## FOR LOGIN / AUTHENTICATION -- auth.py
@app.get("/")
def root():
    return {"message": "Campus Quest API is running "}

@app.post("/auth/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.user_email == data.email).first()
    if existing_user:
        return {"error": "Email already exists"}
        
    hashed = hash_password(data.password)
        
    new_user = User(
        username = data.username,
        user_email = data.email,
        user_password = hashed,
        name = data.name,
    )
    
    db.add(new_user)
    db.commit()
    return {"message": "User successfully created!"}

@app.post("/auth/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.user_email == data.email).first()
    
    if existing_user and verify_password(data.password, existing_user.user_password):
        return {"message": "Login successful!", "token": create_token(existing_user.user_id)}
    
    else:
        return {"message": "Credentials does not match"}
    
@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid Token")
    return {"user_id": user_id}


## METHOD FOR CURRENT USER

def get_current_user(token: str = Depends(oauth2_scheme)):
    verification_user_id = verify_token(token)
    if verification_user_id:
        return verification_user_id
    else:
        raise HTTPException(status_code=401, detail="Invalid User")
    
## FOR QUESTS / quest.py

@app.get("/quests")
def show_quests(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
        user_quests = db.query(Quest).filter(Quest.user_id == user_id).all()
        return user_quests
        
@app.post("/quests")
def create_quests(data: QuestRequest, user_id: int = Depends(get_current_user),  db: Session = Depends(get_db)):
        new_quest = Quest(
            quest_name = data.quest_name,
            quest_description = data.quest_description,
            xp_earned = data.xp_earned,
            quest_deadline = data.quest_deadline,
            user_id = user_id,
        )
        db.add(new_quest)
        db.commit()
        
        return {"message": "Quest successfully created!",
                "user_id": user_id}
    
@app.get("/quests/{quest_id}")
def show_specific_quest(quest_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
        quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
        if not quest:
            raise HTTPException(status_code=404, detail="Record does not exist")
        if quest.user_id != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized access")
        else:
            return quest

@app.put("/quests/{quest_id}")
def update_specific_quest(quest_id: int, data: QuestRequest, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
        quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
        if not quest:
            raise HTTPException(status_code=404, detail="Record does not exist")
        if quest.user_id != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized Access")
        else:
            quest.quest_name = data.quest_name
            quest.quest_description = data.quest_description
            quest.xp_earned = data.xp_earned
            quest.quest_deadline = data.quest_deadline

            db.commit()
            db.refresh(quest)
    
        return{
            "message": "Quest updated successfully",
             "quest": quest_id,
        }
    
@app.delete("/quests/{quest_id}")
def delete_specific_quest(quest_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    
       quest = db.query(Quest).filter(Quest.quest_id == quest_id).first()
       if not quest:
           raise HTTPException(status_code=404, detail="Record does not exist")
       if quest.user_id != user_id:
            raise HTTPException(status_code=403, detail="Unauthorized Access")
       else:
            db.delete(quest)
            db.commit()
            
       return{
            "message": "Quest deleted successfully",
        }
