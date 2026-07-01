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
class LoginResponse(BaseModel):    
    token: str
    