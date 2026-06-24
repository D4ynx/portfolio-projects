from pydantic import BaseModel

class RegisterRequest(BaseModel):
    username : str
    name : str
    email : str
    password : str
    
class LoginRequest(BaseModel):
    email : str
    password : str