import uvicorn
from datetime import datetime
from typing import List
from fastapi import FastAPI, Body 
from uuid import uuid4, uuid1
from pydantic import BaseModel, UUID4, Field

app = FastAPI()
 

class Movie:
    id: UUID4
    name: str
    description: str
    cast: List[str] 
    music_director: str 
    rating: float
    created_at: str
    updated_at: str

    def __init__(self, id, name, description, cast, music_director, rating, created_at, updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.cast = cast
        self.music_director = music_director
        self.rating = rating
        self.created_at = created_at
        self.updated_at = updated_at

class MovieRequest(BaseModel):
    id: UUID4 
    name: str | None = Field(
        default=None, title="The movie name here"
    )
    description: str = Field(max_length=150)
    cast: list[str] 
    music_director: str = Field(max_length=50)  
    rating: float = Field(
        gt=0, le=5, description='The rating must lie between 1 to 5!'
    )
    created_at: datetime 
    updated_at: datetime 
    

now = datetime.now().isoformat()
#dummy in memory db
movies_db = [ 
        Movie(uuid1(), "The Last Horizon", "An epic adventure across time and space.", ["Emily Blunt", "John David Washington"], "Hans Zimmer", 8.7, now, now),
        Movie(uuid4(), "Rhythm of the Heart", "A touching story of love and music.", ["Zendaya", "Oscar Isaac"], "Ludwig Göransson", 7.9, now, now),
        Movie(uuid4(), "Quantum Thief", "A hacker joins a high-stakes digital heist.", ["Rami Malek", "Anya Taylor-Joy"], "Trent Reznor", 8.3, now, now),
        Movie(uuid4(), "Crimson Skies", "Pilots fight for freedom in an alternate 1930s.", ["Tom Hardy", "Margot Robbie"], "Junkie XL", 7.8, now, now),
        Movie(uuid4(), "Echoes in the Fog", "Detectives unravel secrets in a misty town.", ["Benedict Cumberbatch", "Jessica Chastain"], "Max Richter", 8.1, now, now),
]


@app.get("/")
def home():
    return {"message": "Welcome to the Movies API!"}

@app.get("/movies") 
def get_movies(offset: int = 0, limit: int = 10):
    return movies_db[offset: limit]

@app.post("/create-movie")
def create_movie(movie_req: MovieRequest ):
    # if "name" not in movies:
    #     return {"message": "Invalid movie name. Please try again loser", "status": "fail"}
    return movies_db.append(Movie(**movie_req.model_dump()))
    print(typeof(new_movies))


@app.put('/update-movie')
def update_movie(movies=Body()):
    for i in range(len(movies_db)):
        if movies['id'] == movies_db[i]['id']:
            movies_db[i] = movies 
            return {
                "status": "success",
                "message": f"updated '{movies["id"]}' id successfully!",
                "data": movies_db
            }
    return {
        "status": "fail",
        "message": "updation failed due to invalid id! please try again" 
    }

    
@app.delete('/delete-movie/{movie_id}')
def delete_movie(movie_id):
    for i in range(len(movies_db)):
        if movie_id[i] in movies_db[i]["id"]:
            # movies_db.remove(movie_id)
            movies_db.remove(movies_db[i])
            return {
                "status": "success",
                "message": f"deleted '{movie_id}' id successfully!",
                "data": movies_db
            }
    return {
        "status": "fail",
        "message": "invalid id! please try again with an existing id"
    }

@app.delete("/delete-all")
def delete_all_movies(user: str = "guest"):
    if user == "admin":
        movies_db.clear() 
        return {
            "status": "success", 
            "message": "in memory db cleared successfully!",
            "data": movies_db
        }
    else:
        return {
            "You are not allowed to perform this action!"
        }

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", 
        host="0.0.0.0",
        port=22000, 
        log_level="info",
        reload=True,
    )
