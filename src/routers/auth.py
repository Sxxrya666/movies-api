from db.db import get_db 
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from db.models import Users
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timedelta
from enum import Enum
from passlib.context import CryptContext # for password hashing
from fastapi.security import OAuth2PasswordRequestForm
from utils import gen_access_tkn 
from utils.decode_jwt import decode_jwt




router = APIRouter(
    prefix="/auth", 
    tags=["auth"]
)

# enum
class Gender(str, Enum):
    male= "Male"
    female = "Female"

# enum
class Role(str, Enum): 
    guest = "Guest"
    moderator = "Moderator"
    admin =  "Admin"

class Token(BaseModel):
    access_token: str
    token_type :str

class UserRequest(BaseModel):
    first_name : str 
    last_name : str 
    email : EmailStr 
    password : str 
    role : Role = Role.guest
    gender: Gender = Gender.male 
    created_at : datetime 

db_inject= Annotated[Session, Depends(get_db)]
auth_chk_inject = Annotated[Token, Depends(decode_jwt)]
password_context = CryptContext(schemes=["bcrypt"], deprecated=['auto'])

@router.get("/users", status_code=200)
def get_all_users(db: db_inject):
    return db.query(Users).all()

@router.post("/sign-up", status_code=201)
def sign_up( user_req: UserRequest,  
             db: db_inject):

    existing_email = db.query(Users).filter(user_req.email == Users.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email is already registered. Please try with a non-existing email!")

    user_body = Users(
        first_name=user_req.first_name,
        last_name=user_req.last_name,
        email=user_req.email,
        hashed_password=password_context.hash(user_req.password), 
        role=user_req.role,
        gender=user_req.gender,
        created_at=user_req.created_at,
    )
    db.add(user_body)
    db.commit()
    db.refresh(user_body)
    return user_body

def authenticate_user(email, password, db):
    user = db.query(Users).filter(email == Users.email).first()
    if not user:  
        return None 

    # problem here.
    hashed_passwd = user.hashed_password
    dehashed_pass = password_context.verify(password, hashed_passwd)
    if not dehashed_pass:
        return None
    return user

@router.post("/login", response_model=Token)
def user_login( db: db_inject, 
                form: OAuth2PasswordRequestForm = Depends()):
    try: 
        user_input = authenticate_user(form.username, form.password, db)
        if user_input is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="user_input is returing None bruh! why?")
        print(f'{user_input=}');
        token = gen_access_tkn.gen_access_token(user_input.email, user_input.id, timedelta(minutes=15))
        return {
            "access_token": token,
            "token_type": "Bearer"
        }
    except: 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                            , detail="CRITICAL ERROR OCCURED WHEN LOGGING YOU IN!")