from sqlalchemy.orm import DeclarativeBase, mapped_column
from db.db import engine
from sqlalchemy import Integer, Column, Float, String, DateTime 

class Base(DeclarativeBase):
    pass

class MovieRating(Base):
    __tablename__ = 'movie_rating'
    id = mapped_column(Integer, primary_key=True,autoincrement=True, index=True)
    name = Column(String(40))
    description = Column(String(100))
    cast = Column(String(20)) 
    music_director = Column(String(40)) 
    rating = Column(Float) 
    release_year = Column(DateTime)
    created_at = Column(String(40))
    updated_at = Column(String(40))


print('creating tables..')
MovieRating.metadata.create_all(bind=engine)
print('created tables successfully!')
