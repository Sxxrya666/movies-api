import uvicorn
from datetime import datetime
from typing import List
from fastapi import FastAPI, Body , Path, Query, HTTPException
from uuid import uuid4, uuid1
from pydantic import BaseModel, UUID4, Field
from starlette import status


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
 

class Movie:
    id: UUID4
    name: str
    description: str
    cast: List[str] 
    music_director: str 
    rating: float
    release_year: datetime
    created_at: str
    updated_at: str

    def __init__(self, id, name, description, cast, music_director, rating, release_year, created_at, updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.cast = cast
        self.music_director = music_director
        self.rating = rating
        self.release_year = release_year
        self.created_at = created_at
        self.updated_at = updated_at

class MovieRequest(BaseModel):
    id: UUID4 = Field(uuid4() )
    name: str | None = Field(
        default=None, title="The movie name here"
    )
    description: str = Field(max_length=150)
    cast: list[str] 
    music_director: str = Field(max_length=50)  
    rating: float = Field(
        gt=0, le=5, description='The rating must lie between 1 to 5!'
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
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Inception",
                "description": "A mind-bending thriller about dreams within dreams.",
                "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
                "music_director": "Hans Zimmer",
                "rating": 4.8,
                "release_year": "2022",
                "created_at": "2025-07-23T10:00:00",
                "updated_at": "2025-07-23T12:00:00"
            }
        }
    }
    

now = datetime.now().isoformat()
year = str(datetime.today().year)
#dummy in memory db
movies_db = [ 
        Movie(str(uuid4()), "The Last Horizon", "An epic adventure across time and space.", ["Emily Blunt", "John David Washington"], "Hans Zimmer", 4.5,year, now, now),
        Movie(str(uuid4()), "Rhythm of the Heart", "A touching story of love and music.", ["Zendaya", "Oscar Isaac"], "Ludwig Göransson", 2.1, year, now, now),
        Movie(str(uuid4()), "Quantum Thief", "A hacker joins a high-stakes digital heist.", ["Rami Malek", "Anya Taylor-Joy"], "Trent Reznor", 5, year, now, now),
        Movie(str(uuid4()), "Crimson Skies", "Pilots fight for freedom in an alternate 1930s.", ["Tom Hardy", "Margot Robbie"], "Junkie XL", 4.5, year, now, now),
        Movie(str(uuid4()), "Echoes in the Fog", "Detectives unravel secrets in a misty town.", ["Benedict Cumberbatch", "Jessica Chastain"], "Max Richter", 2.1, year, now, now),
        Movie(str(uuid4()), "Echoes in the Fog", "Detectives unravel secrets in a misty town.", ["Benedict Cumberbatch", "Jessica Chastain"], "Max Richter", 2.1, year, now, now),
]


@app.get("/")
async def home():
    return {"message": "Welcome to the Movies API!"}


@app.get("/movies", status_code=200) 
async def get_movies(offset: int = 0, limit: int = 10):
    return movies_db[offset: limit]

@app.get("/movies/{movie_id}", status_code=200)
async def get_single_movie(movie_id):
    for movie in movies_db:
        if str(movie.id) == movie_id:
            return movie
    raise HTTPException(status_code=400, detail="Movie not found! Check ID and try again")

@app.get("/movies/{rating}", status_code=200)
def check(rating: float = Path( gt=0, le=5, description="enter the rating to fetch movies") ):
    tmp_rated_movies = []
    for i in range(len(movies_db)):
        if rating == movies_db[i].rating:
            tmp_rated_movies.append(movies_db[i])
    return  {"status": "success", "data": tmp_rated_movies}
    raise HTTPException(status_code=400, item='query params is either invalid or item unavailable')


@app.get("/movies/", status_code=200)
def check(rating: float = Query( gt=0, le=5, description="enter the rating to fetch movies") ):
    tmp_rated_movies = []
    for i in range(len(movies_db)):
        if rating == movies_db[i].rating:
            tmp_rated_movies.append(movies_db[i])
    return  {"status": "success", "data": tmp_rated_movies}
    raise httpException(status_code=401, item='url param is either invalid or item unavailable')

@app.post("/create-movie", status_code=201)
async def create_movie(movie_req: MovieRequest ):
    if movie_req:
        return movies_db.append(Movie(**movie_req.model_dump()))
    raise HTTPException(status_code=400, detail=f"Error creating movie: {str(e)}")

@app.put('/update-movie', status_code=200)
async def update_movie(movie: MovieRequest):
    for i in range(len(movies_db)):
        if str(movie.id) == movies_db[i].id:
            movies_db[i] = movie 
            return {
                "status": "success",
                "message": f"updated movie data successfully!",
                "data": movies_db
            }
    raise HTTPException(status_code=400, detail="Item not found! Check ID and try again")  

    
@app.delete('/delete-movie/{movie_id}', status_code=204)
async def delete_movie(movie_id):
    for i in range(len(movies_db)):
        if movie_id in movies_db[i].id:
            # movies_db.remove(movie_id)
            movies_db.remove(movies_db[i])
            return {
                "status": "success",
                "message": f"deletion successfully!",
                "data": movies_db
            }
    raise HTTPException(status_code=401, detail="invalid url parameter or item unavailable")

@app.delete("/delete-all", status_code=200)
async def delete_all_movies(user: str = "guest"):
    if user == "admin":
        movies_db.clear() 
        return {
            "status": "success", 
            "message": "in memory db cleared successfully!",
            "data": movies_db
        }
    return HTTPException(status_code=403, detail="you are not alloe to perform this action")
if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", 
        host="0.0.0.0",
        port=22000, 
        log_level="info",
        reload=True,
    )
