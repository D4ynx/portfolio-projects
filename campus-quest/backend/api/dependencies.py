from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from services.auth_services import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

## METHOD FOR CURRENT USER (TOKEN)
def get_current_user(token: str = Depends(oauth2_scheme)):
    verification_user_id = verify_token(token)
    if verification_user_id:
        return verification_user_id
    else:
        raise HTTPException(status_code=401, detail="Invalid User")
    
