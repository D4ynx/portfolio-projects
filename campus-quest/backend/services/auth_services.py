import bcrypt
from jose import jwt
from datetime import datetime, timedelta


## PASSWORD AND TOKENIZATION
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

## FUNCTIONS

def hash_password(password):
    encoded_password = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password.decode()

def verify_password(password, hashed_password):
    verification = bcrypt.checkpw(password.encode(), hashed_password.encode())
    return verification

def create_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_token["user_id"]
