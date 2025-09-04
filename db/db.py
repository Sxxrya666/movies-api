from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("MYSQL_USERNAME")
db_pass = os.getenv("MYSQL_PASSWORD")
db_name = os.getenv("MYSQL_DBNAME")

mysql_conn_url = f"mysql+mysqlconnector://{db_username}:{db_pass}@localhost/{db_name}"
engine = create_engine(mysql_conn_url, echo=True)

SessionLocal = sessionmaker(autoflush=False, bind=engine )

db = SessionLocal()

def get_db():
    try: 
        yield db
    finally: 
        db.close()