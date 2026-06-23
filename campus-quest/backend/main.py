from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from db.database import engine, Base, get_db
from models.user import User 
from api.auth import hash_password, verify_password, create_token, verify_token
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class RegisterRequest(BaseModel):
    username : str
    name : str
    email : str
    password : str
    
class LoginRequest(BaseModel):
    email : str
    password : str

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

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
        raise HTTPException(status_code=401, details="Invalid Token")
    return {"user_id": user_id}