from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from configs.keys import settings 

engine = create_engine(settings.db_url, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine )


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()