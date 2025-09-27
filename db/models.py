from sqlalchemy.orm import DeclarativeBase, mapped_column
from .db import engine
from sqlalchemy import BigInteger, Column, Float, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import ENUM

class Base(DeclarativeBase):
    pass

class MovieRating(Base):
    __tablename__ = 'movie_rating'
    id = mapped_column(BigInteger, primary_key=True,autoincrement=True, index=True)
    name = Column(String(40))
    description = Column(String(100))
    cast = Column(String(20)) 
    music_director = Column(String(40)) 
    rating = Column(Float) 
    release_year = Column(DateTime)
    created_at = Column(String(40))
    updated_at = Column(String(40))
    reviewed_by = Column(BigInteger, ForeignKey("users.id"))



class Users(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True) 
    first_name = Column(String(200), default="Anonymous") 
    last_name =  Column(String(200), default="User") 
    email = Column(String(200), unique=True, index=True) 
    hashed_password= Column(String(200)) 
    phone_number = Column(String(20), index=True, unique=True)
    role = Column(
        ENUM("Admin", "Guest", "Moderator"),
        index=True
    ) 
    gender = Column(ENUM("Male", "Female"), index=True) 
    created_at = Column(DateTime) 
    
    

def create_tables():
    Base.metadata.create_all(bind=engine)
