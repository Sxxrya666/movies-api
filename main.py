import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import auth, movie_rating
from db.models import create_tables 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('inside lifespan func')
    print('creating tables...')
    create_tables()
    yield
    print('table creation successful')



app = FastAPI(
    lifespan=lifespan,
    swagger_ui_parameters={"tryItOutEnabled": True}
    )


@app.get("/")
async def home():
    return {"messagee": "Welcome to the Movies API!"}

API_VERSION = "v1"
app.include_router(movie_rating.router, prefix=f"/api/{API_VERSION}")
app.include_router(auth.router, prefix=f"/api/{API_VERSION}")


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", 
        log_level="info",
        port=22000,
        # reload=True,
    )
