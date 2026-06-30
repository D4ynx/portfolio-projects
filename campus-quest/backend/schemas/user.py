from pydantic import BaseModel, ConfigDict
from datetime import date
from enum import Enum

class StreakStatusEnum(Enum):
    active = "active"
    broken = "broken"
    retained = "retained"
    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id : int
    username : str
    user_email : str
    name: str
    user_xp: int
    user_streak: int
    level : int
    
class UserUpdateRequest(BaseModel):
    username : str
    name: str
    
class UserXPResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: int
    username : str
    user_xp: int
    user_streak: int
    level: int
    user_xp_needed: int
    
class UserStreakResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    streak_id: int
    user_id : int
    streak_count : int
    streak_date : date
    status : StreakStatusEnum
    streak_restore : int