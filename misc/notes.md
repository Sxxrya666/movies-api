
## misc shit (project setup etc)
1. how to install deps in uv without requriements.txt?
> use => `uv sync` === pip install -r requirements.txt 
2. use `reload = True in 
3. for uuid4 in pydantic, just import `UUID4` from pydantic
4. `type` keyword in python. 
> example: `type db_dep = Annotated[Session, Depends(get_db)]` 
> its saying: *"From now on, whenever I write db_dep, what I really mean is that long, ugly thing: Annotated[Session, Depends(get_db)]."*
5. import `EmailStr` from pydantic to validate email

6. to clear out all record from db, use this command: 
7. to mount endpoints inside a route, use this inside `APIRouter()` function
```python
APIRouter(
    prefix="/auth", # matlab the 'PREFIX' route. pehle kya chahiye actual endpiont ke pehle
    tags=[''], # A list of tags to be applied to all the path operations in this router.
    
)
```

```sql
truncate <table_name>
```

7. `response_model=` parameter is used to control what data is sent to the user, just like projection i think . used in decorators like app.post, put, get, delete
<details>
    <summary>LEARN more</summary>
    Filters Data: It automatically removes any data from your output that isn't defined in the model (like the password in our example). This is great for security.

    Validates Data: It ensures the data you're sending out matches the types you promised (e.g., that an id is an integer, not a string).


    Converts Data: It takes your raw Python data (like a dict or database object) and properly converts it into a JSON response.

    Documents Your API: It automatically generates a precise schema for your API response in the documentation (e.g., at /docs), which is extremely helpful for anyone using your API.

</details>

## path parameters
- same bs that make the url dynamic like url params in express 
- syntax: app.get("/some-route/{some_var}")
    - use {variable_name} for dynamic shit
### path validation using `Path()` from fastapi
- use Path(min_val,max_val, ...) and other shit to validate what's within the url path: 
for eg: `localhost:3880/movies/{movies_id}
enforce those shit for url to behave strictly when taking url params
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

## model config
- why use this? 
> it will help pre-populate the json for request to server
- use it inside the req class like this : 
```python
{
    "json_schema_extra": {
        "example": {
            "field": "value",
            "field2": "value2"
            ...
        }
    }
}
```

 - i can configure swagger docs to behave my way. eg i changed this in the fastapi instance
```python
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
```
> why ? becuase it was annoying to click the "try it now" button time and again




# SQLALCHEMY

## Architecture Notes (The "Where") 📂
-   **Example:**
    
    -   `main.py`: This will hold the main FastAPI app and the API routes (`@app.get`, `@app.post`, etc.).
        
    -   `database.py`: This is just for the database connection setup (the `engine`, `SessionLocal`, and `Base`).
        
    -   `models.py`: This will define the shape of my database tables using SQLAlchemy (e.g., the `User` class).
        
    -   `schemas.py`: This will define the shape of my API data using Pydantic (e.g., what a `UserCreate` request should look like).




- for mysql, use dialect called 'mysqlconnector' liek this `mysql+mysqlconnector://...`  to connect engine 
> format: `mysql+mysqlconnector://username:pass@localhost:[root_optional]/database_name`

- always first engine.connect(), then .execute(<some_sql_query>), then commit()
- dont write manual sql, instead use alchemy's core: 
  - import TABLE, METADATA, COLUMN etc (other datatypes such as STRING, INTEGER, FLOAT etc)
    > for string, you have to give string(<some_length>) just like varchar or else error will come
  - use constraints such as `primary_key=True/False` , `autoincrement=True`, `nullable=True/false` etc
  - i can insert multiple objects using list `[{...}, {...}, ...]` using the `insert().values()` method

- use `DeclarativeBase` to define data schema for database
    - inherit the baseclass to your customclass that you will define schema in: 
    ```
    class SomeClass(DeclarativeBase):
        pass
    ```
    - pass this thing called `__tablename__` = 'the table name you want'
- THEN, when you see Base.metadata.create_all(engine), it simply means:
> *"Hey, SQLAlchemy! Go look at all the table blueprints (.metadata) I've defined using my Base class, and then build all those tables in the database that this engine is connected to."*
- to use db in any endpiont, you have to first inject the dependancy (the sessionLocal thing) in the route handler. 
- then yield it and close it after connection is received. 
### query a db 
- `db.query(TableName).all()` is the 'select * from ...'
- `db.query().filter(do some filtration).all()
- for post request, first add to session then commit to make change to db. atomicity of TRANSACTION!!

- for put request, get input , check db if the id is same as db.id, then overwrite the db's columns for that id. then add + commit
- db.add(<you must put the query inside this>)
- .delete() method: to delete the entire object. 


## authentication
- use bcrypt to hash the password
- `from passlib.context import CryptContext` this will create a password manager that will create a context for what algo i m using to hash the password as. Like a settings tweaker for the algo im using
- then pass these params to the class => CryptContext(schemes=['bcrypt'], deprecated=['auto']) . scheme will tell what type of algo, deprecated is __ idk 
- then encode it using the jwt.encode() method given by the jose crypto library to mint expiry time + body inside jwt
> SYNTAX; jwt.encode(payload, algo, secret_key_or_sum)

## authorization
- just write an authenticate_user func to check if email and pass exist in db. 
- use .verify(plainpass, db-ka-hashed-pass) method on the context to see if pass exist in db
- same for email
- use oauth2passwordrequestform from fastapi.security to get form for auth. 
- inject it as a type and return the fields from it to the user
- in the route handler, for login, take email and pass from user and pass it as args to the util func i made earlier
- return email and pass from the form argument of type oauth2 of specific fields back as response