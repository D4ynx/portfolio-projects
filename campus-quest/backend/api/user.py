from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_current_user
from db.database import get_db
from models.user import User
from schemas import UserUpdateRequest, UserResponse
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