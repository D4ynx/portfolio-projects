from pydantic import BaseModel, ConfigDict

## Pydantic Models - Request
class RegisterRequest(BaseModel):
    username : str
    name : str
    email : str
    password : str
    
class LoginRequest(BaseModel):
    email : str
    password : str
    
## Pydantic Models - Response
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id : int
    username : str
    user_email : str
    name: str
    user_xp: int
    user_streak: int
    
class LoginResponse(BaseModel):    
    token: str
