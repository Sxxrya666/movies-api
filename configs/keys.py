import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings 

load_dotenv()

class Settings(BaseSettings):
    jwt_key: str | None = os.getenv("JWT_KEY")
    jwt_algo: str | None = os.getenv("JWT_ALGORITHM")
    db_url: str | None = os.getenv("MYSQL_DB_URL") 
    API_VERSION: int = 1 

    class Config:
        env_file: ".env"

settings = Settings()
