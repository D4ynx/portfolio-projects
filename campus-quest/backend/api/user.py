from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_current_user
from db.database import get_db
from models.user import User
from services.auth_services import get_user_by_id 
from services.xp_services import calculate_level, xp_cap
from schemas import UserUpdateRequest, UserResponse, UserXPResponse
from sqlalchemy.orm import Session

router = APIRouter()

## ENDPOINTS

@router.get("/me", response_model = UserResponse)
def show_user(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "Record does not exist")
    return user


@router.put("/me", response_model = UserResponse)
def update_user(data: UserUpdateRequest, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    
    user.username = data.username
    user.name = data.name

    db.commit()
    db.refresh(user)
        
    return user

@router.get("/me/level", response_model = UserXPResponse)
def update_level(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    xp = user.user_xp
    level = calculate_level(xp)
    
    xp_needed = xp_cap(level + 1) - user.user_xp
    
    level_information = {
        "user_id" : user.user_id,
        "username" : user.username,
        "user_xp" : xp,
        "user_streak": user.user_streak,
        "level" : level,
        "user_xp_needed" : xp_needed,
    }
    
    return level_information
    