from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from db.models import MovieRating 
from db.db import get_db 
from utils.decode_jwt import decode_jwt
from routers.auth import Token

router = APIRouter(
    tags=["movie"]
) 

class MovieRatingRequest(BaseModel):
    # id: int  
    name: str | None = Field(
        default=None, title="The movie name here"
    )
    description: str = Field(max_length=150)
    cast: str 
    music_director: str = Field(max_length=50)  
    rating: float = Field(
        gt=0, le=10, description='The rating must lie between 1 to 10!'
    )
    release_year: datetime = Field(
        default=datetime.today().year,
        description="The release date of the movie in YYYY-MM-DD format."
    ) 
    created_at: datetime = Field(default=datetime.now().isoformat(), description="The date and time when the movie was created.")
    updated_at: datetime = Field(default=datetime.now().isoformat(), description="The date and time when the movie was last updated.")

    # MODEL CONFIG
    model_config = {
        "json_schema_extra": {
            "Example Body": {
                "id": 420,
                "name": "Inception",
                "description": "A mind-bending thriller about dreams within dreams.",
                "cast": "Some Guy", 
                "music_director": "Hans Zimmer",
                "rating": 4.8,
                "release_year": "2022",
                "created_at": "2025-07-23T10:00:00",
                "updated_at": "2025-07-23T12:00:00"
            }
        }
    }
    
db_inject= Annotated[Session, Depends(get_db)]
get_curr_user = Annotated[Token, Depends(decode_jwt)]

@router.get("/movies", status_code=200) 
async def get_movies(curr_user: get_curr_user, db: db_inject):
    obj =  db.query(MovieRating).all()
    return obj 

@router.get("/movies/{movie_id}", status_code=200)
async def get_single_movie( movie_id: int,
                            current_user: get_curr_user,
                            db : db_inject):

    req_obj = db.query(MovieRating).filter(MovieRating.id == movie_id).first()
    
    if not current_user.get("subject"):
        raise HTTPException(status_code=400, detail="Malformed or incomplete token!", location="/movies/{movie_id}")

    if not req_obj: 
        raise HTTPException(status_code=400, detail="Movie not found! Check ID and try again")
    return req_obj

@router.post("/create-movie", 
             status_code=201, 
             )
async def create_movie( movie_req: MovieRatingRequest, 
                        db: db_inject,
                        current_user : get_curr_user
                       ):
    req_obj = MovieRating(**movie_req.model_dump())
    #get the id from jwt token  
    user_id = current_user.get("subject")
    if not user_id: 
        raise HTTPException(
            status_code =status.HTTP_401_UNAUTHORIZED,
            detail="Malformed token! Failed to perform user authentication"
        )

    if not req_obj:
        raise HTTPException(status_code=400, detail=f"Something went wrong while creating the review")
    db.add(req_obj)
    db.commit()
    db.refresh(req_obj) 
    return req_obj

@router.put('/update-movie/{movie_id}', status_code=200)
async def update_movie(movie_id: int,
                       movie_req: MovieRatingRequest,
                       current_user: get_curr_user,
                       db: db_inject):
    req_obj = db.query(MovieRating).filter(MovieRating.id == movie_id).first()
    
    user_id = current_user.get("subject")
    if not user_id: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Malformed or expired token! Try logging in again." ) 

    if not req_obj:
        raise HTTPException(status_code=400, detail="Item not found! Check ID and try again")  
    
    req_obj.name = movie_req.name  
    req_obj.description = movie_req.description  
    req_obj.cast = movie_req.cast  
    req_obj.music_director = movie_req.music_director  
    req_obj.rating = movie_req.rating  
    req_obj.release_year = movie_req.release_year  
    req_obj.created_at = movie_req.created_at  
    req_obj.updated_at = movie_req.updated_at  
    
    db.add(req_obj)
    db.commit()
    
@router.delete('/delete-movie/{movie_id}', status_code=204)
async def delete_movie(movie_id: int,
                       current_user: get_curr_user,
                       db: db_inject):
    req_obj = db.query(MovieRating).filter(movie_id == MovieRating.id).first()

    user_id = current_user.get("subject")
    if not user_id: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Malformed or expired token! Try logging in again." ) 

    if not req_obj:
        raise HTTPException(status_code=500,detail="Could not delete the specified rating" ) 
    
    db.query(MovieRating).filter(movie_id == MovieRating.id).delete()
    db.commit()


@router.delete("/delete-all", status_code=204)
async def delete_all_movies(current_user: get_curr_user,
                            db: db_inject):
    db.query(MovieRating).delete() 
    db.commit()
    

