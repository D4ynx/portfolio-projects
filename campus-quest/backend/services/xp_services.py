from models.user import User
from sqlalchemy.orm import Session
from services.auth_services import get_user_by_id

from constants import BASE_XP, XP_MULTIPLIER, EXPONENT

def calculate_xp (streak: int):
    calculated_xp = BASE_XP * (XP_MULTIPLIER * streak + 1)
    return calculated_xp

def xp_cap(level: int):
    xp_cap = BASE_XP * (level ** EXPONENT)
    return xp_cap 

def calculate_level(xp: int):
    level = 1
    
    while xp >= xp_cap(level):
        level = level + 1
        
    return level

def save_xp (streak: int, user_id:int, db: Session):
    user = get_user_by_id(user_id, db)
    add_xp = calculate_xp(streak)
    
    user.user_xp = user.user_xp + add_xp

    db.commit()
    db.refresh(user)
    
    return user.user_xp
    