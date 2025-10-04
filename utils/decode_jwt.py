from fastapi.security import OAuth2PasswordBearer 
from fastapi import Depends, HTTPException
from jwt import decode
from jwt.exceptions import InvalidTokenError
import os
from configs.keys import settings 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/api/v{settings.API_VERSION}/auth/login") 

def decode_jwt(token: str = Depends(oauth2_scheme)):
    
    try:
        decoded_tkn = decode(token, settings.jwt_key, settings.jwt_algo)
        return decoded_tkn
    except InvalidTokenError:  # using invalidTokenError class
        return HTTPException(status_code=401, detail="Invalid Token Boss! Session expired or incorrect credentials")