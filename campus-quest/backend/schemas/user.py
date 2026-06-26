from pydantic import BaseModel, ConfigDict

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