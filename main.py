from fastapi import FastAPI, Body
from uuid import uuid4, UUID


app = FastAPI()

#dummy in memory db
movies_db = [ ]


@app.get("/")
def home():
    return {"message": "Welcome to the Movies API!"}

@app.get("/movies") 
def get_movies(offset: int = 0, limit: int = 10):
    return movies_db[offset: limit]

@app.post("/send-movie")
def send_movie(movies=Body()):
    if "movie_name" not in movies:
        return {"message": "Invalid movie name. Please try again loser", "status": "fail"}
    return movies_db.append({"id": str(uuid4()), "movie_name": movies['movie_name']})

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
