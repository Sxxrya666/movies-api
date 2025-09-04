from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from config.keys import db_username, db_password, db_name
import os

load_dotenv()

mysql_conn_url = f"mysql+mysqlconnector://{db_username}:{db_password}@localhost/{db_name}"
engine = create_engine(mysql_conn_url, echo=True)

SessionLocal = sessionmaker(autoflush=False, bind=engine )


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()