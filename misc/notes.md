
## misc shit (project setup etc)
1. how to install deps in uv without requriements.txt?
> use => `uv sync` === pip install -r requirements.txt 
2. use `reload = True in 
3. for uuid4 in pydantic, just import `UUID4` from pydantic

## path parameters
- same bs that make the url dynamic like url params in express 
- syntax: app.get("/some-route/{some_var}")
    - use {variable_name} for dynamic shit

## query params
- When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
- your typical `url.com?key=value` syntax

## POST
- send body using the `Body()` method . (import from fastapi module) 
- can use f strings in return statements like this: 

```python
return {
    "message": f"operation '{something}' done successfully!",
}
``` 

# pydantic
- create a request class upon the actual class, which is the request ka schema.
- then inherit the baseClass given by pydantic to that request class to use its validation features 
eg: Movie class will be as MovieRequest class or sum. 

🤔 **"Why use `model_dump()` if the incoming request is already JSON?"**
```python
@app.post("/create-movie")
def create_movie(movie_req: MovieRequest ):
    new_movies = Movie(**movie_req.model_dump()) 
```
- this `movie_req` thing is a model instance of PYDANTIC!! so it will look sum like tis: 
- new_movies = Movie(**movie_req.model_dump()) 
# Incoming raw JSON → parsed by FastAPI
movies = MovieRequest(name="Inception", year=2010, director="Christopher Nolan")

### 🧠 FastAPI Automatically Converts This:

```python
# Incoming raw JSON → parsed by FastAPI
movies = MovieRequest(name="Inception", year=2010, director="Christopher Nolan")
```

Now `movies` is **NOT a dictionary**, it's a **Pydantic model instance**, which behaves like:

```python
class MovieRequest(BaseModel):
    name: str
    year: int
    director: str
```

So this line:

```python
Movie(**movies)
```

🔴 **Will raise an error** like:

```
TypeError: type object argument after ** must be a mapping, not MovieRequest
```

Because `**movies` tries to unpack a model, which is not a dict.

---

## Field validation
- use the Field method to validate value in obj 
- eg: `Field(
            min_length=, 
            max_length=,
            gt=, 
            lt=
        )
