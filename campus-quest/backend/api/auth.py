from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import Depends, HTTPException, APIRouter
from schemas import RegisterRequest, LoginRequest, UserResponse, LoginResponse
from models.user import User
from services.auth_services import hash_password, verify_password, create_token
from api.dependencies import get_current_user

router = APIRouter()

## ENDPOINTS
@router.post("/register", response_model = UserResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.user_email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")
        
    hashed = hash_password(data.password)
        
    new_user = User(
        username = data.username,
        user_email = data.email,
        user_password = hashed,
        name = data.name,
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login", response_model = LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.user_email == data.email).first()
    
    if existing_user and verify_password(data.password, existing_user.user_password):
        return {"token": create_token(existing_user.user_id)}
    
    else:
        raise HTTPException(status_code=401, detail= "Credentials does not match")
    
@router.get("/protected")
def protected(user_id: int = Depends(get_current_user)):
    return {"user_id": user_id}