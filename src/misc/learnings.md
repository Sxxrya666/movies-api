## error 1: 
![alt text](images/image.png)

---
# ERROR: 2

## 📥 Input Code
```python
def send_items(items: Body()):
# also this too 
def send_items(items: Body):
```

## 📤 Error Output
```python
fastapi.exceptions.FastAPIError: Invalid args for response field! Hint: check that annotation=NoneType required=True json_schema_extra={} is a valid Pydantic field type. If you are using a return type annotation that is not a valid Pydantic field (e.g. Union[Response, dict, None]) you can disable generating the response model from the type annotation with the path operation decorator parameter response_model=None. Read more: https://fastapi.tiangolo.com/tutorial/response-model/
```

## ✅ Solution
```diff
-def send_items(items: Body):
+def send_items(items: dict  = Body()):
OR
+def send_items(dict=Body()):
```

## 📝 Analysis
**Root Cause:** 
i tried to use Body() as a type. bruh. 
## 🔗 Resources
- N/A

---
# ERROR: 3

## 📥 Input Code
```python
fake_items_db = {
    "items": {
        {"id": str(uuid4()), "item_name": "balls"}, 
        {"id": str(uuid4()), "item_name": "Milk"}, 
        {"id": str(uuid4()), "item_name": "Cucumber"}
    }
}
```

## 📤 Error Output
```python
Set entry must be hashable
  Type "dict[str, str]" is not hashablePylancereportUnhashable

```

## ✅ Solution
```diff
-fake_items_db = {
+fake_items_db = [
    "items": {
        {"id": str(uuid4()), "item_name": "balls"}, 
        {"id": str(uuid4()), "item_name": "Milk"}, 
        {"id": str(uuid4()), "item_name": "Cucumber"}
    }
+]
-}
```

## 📝 Analysis
**Root Cause:** 
> use list of dicts. because using {{...}, {...}} is illegal
> so use [{...}, {...}, {...}] 



---
# ERROR: 4

## 📥 Input Code
```python
    fake_items_db.append(str(id))
```

## 📤 Error Output
```python
Argument of type "str" cannot be assigned to parameter "object" of type "dict[str, str]" in function "append"
```

## ✅ Solution
```diff
error
```

## 🔗 Resources
- N/A


---
# ERROR: 5

## 📥 Input Code
```python
fake_items_db = [
    "id": str(uuid4())
        { "item_name": "balls" }, 
    "id": str(uuid4())
        { "item_name": "milk"}, 
    "id": str(uuid4())
        { "item_name": "cucumber"}
]
```

## 📤 Error Output
```python
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/books-api/main.py", line 8
    "id": str(uuid4())
        ^
```

## ✅ Solution
```diff
fake_items_db = [{
    "id": str(uuid4()),
    "item_name": "balls", 
    },
    { 
    "id": str(uuid4()),
    "item_name": "gum"
    },
    {
    "id": str(uuid4()),
    "item_name": "broom"
    }
]
```

## 📝 Analysis
**Root Cause:** 
i didnt fucking know how to even put list of dicts properly and assign ONE KEY multiple vals for it

## 🔗 Resources
- https://www.scaler.com/topics/list-of-dictionaries-in-python/ 


---
# ERROR: 6

## 📥 Input Code
```python
    if not items["item_name"]:
        return {"message": "Invalid item name. Please try again loser", "status": "fail"}

```

## 📤 Error Output
```python
   File "/mnt/e/e-drive/coding/newnew/py/fastAPI/books-api/main.py", line 34, in send_item
    if not items["item_name"]:
           ~~~~~^^^^^^^^^^^^^
KeyError: 'item_name'
```

## ✅ Solution
```diff
-if not items["item_name"]:
+if "item_name" not in dict_name:
    return {"message": "Invalid item name. Please try again loser", "status": "fail"}
```

## 📝 Analysis
**Root Cause:** 

## 🔗 Resources
- gpt: 
> **🧠 Hint Level:**  
If you’re not gonna use `get()`, at least check `if "item_name" in items`. Because right now, your validation logic is like building a bridge and hoping the river doesn’t move.

---
# ERROR: 7

## 📥 Input Code
```python
❯ uv add icecream
```

## 📤 Error Output
```python
warning: `VIRTUAL_ENV=/mnt/e/e-drive/coding/newnew/py/fastAPI/books-api/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
```

## ✅ Solution
```diff

```

---
# ERROR: 8

## 📥 Input Code
```python
if __name__ == "__main__":
    uvicorn.run(
        app,
        "__main__:app", 
        host="0.0.0.0",
        port=22000, 
        log_level="info",
        reload=True,
    )   
```

## 📤 Error Output
```python
error
```

## ✅ Solution
```diff
if __name__ == "__main__":
    uvicorn.run(
-       app,
+       "__main__:app", 
        host="0.0.0.0",
        port=22000, 
        log_level="info",
        reload=True,
    )
```

## 🔗 Resources
- https://github.com/fastapi/fastapi/discussions/7449


---
# ERROR: 9

## 📥 Input Code
```python

```

## 📤 Error Output
```python
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/main.py", line 32, in MovieRequest
    name: str | None = Field(
                       ^^^^^
NameError: name 'Field' is not defined
```

## ✅ Solution
```diff
You never imported it dummy!
```
---
# ERROR: 10

## 📥 Input Code
```python
@app.get("/movies/{movie_id}")
async def get_single_movie(movie_id):
    for movie in movies_db:
        if movie["id"] == movie_id:
            print(type(movie))
            return movie
```

## 📤 Error Output
```python
TypeError: 'Movie' object is not subscriptable
```

## ✅ Solution
```diff
@app.get("/movies/{movie_id}")
async def get_single_movie(movie_id):
    for movie in movies_db:
+       if movie.id == movie_id:
-       if movie["id"] == movie_id:
            print(type(movie))
            return movie
```

## 📝 Analysis
**Root Cause:** 
## 🧠 Why?

Because `movie` is a **class instance**, not a dictionary.

And in Python:

-   Dictionaries use `["key"]` → ✅ `movie["id"]`
    
-   **Objects** (like instances of a class or Pydantic model) use **dot notation** → ✅ `movie.id`
    

So if you try to treat an object like a dictionary, you get that exact **TypeError**.

---
another type 
```python
if movie_id in movies_db[i]["id"]:
    pass
```

> fix
```python
-if movie_id in movies_db[i]["id"]:
    pass
+if movie_id in movies_db[i].id:
    pass
```

---
# ERROR: 11

## 📥 Input Code
```python
def check(rating: Path(default=1, le=1, ge=5, description="enter the rating to fetch movies") ):
```

## 📤 Error Output
```python
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/fastapi/params.py", line 189, in __init__
    assert default is ..., "Path parameters cannot have a default value"
           ^^^^^^^^^^^^^^
AssertionError: Path parameters cannot have a default value
```

## ✅ Solution
```diff
-def check(rating: Path(default=1, le=1, ge=5, description="enter the rating to fetch movies") ):
+def check(rating: Path(le=1, ge=5, description="enter the rating to fetch movies") ):
```
fix

## 📝 Analysis
**Root Cause:** 
description

## 🔗 Resources
- N/A


---
# ERROR: 12

## 📥 Input Code
```python
def check(rating: Path( le=1, ge=5, description="enter the rating to fetch movies") ):
```

## 📤 Error Output
```python
fastapi.exceptions.FastAPIError: Invalid args for response field! Hint: check that annotation=NoneType required=True description='enter the rating to fetch movies' json_schema_extra={} is a valid Pydantic field type. If you are using a return type annotation that is not a valid Pydantic field (e.g. Union[Response, dict, None]) you can disable generating the response model from the type annotation with the path operation decorator parameter response_model=None. Read more: https://fastapi.tiangolo.com/tutorial/response-model/
```

## ✅ Solution
```diff
-def check(rating: Path( le=1, ge=5, description="enter the rating to fetch movies") ):
+def check(rating: int = Path( le=1, ge=5, description="enter the rating to fetch movies") ):
```
fix

## 📝 Analysis
**Root Cause:** 
add a fucking type and ASSSIGN ITT WITH AN '='

## 🔗 Resources
- N/A

---
# ERROR: 13

## 📥 Input Code
```python
    raise HTTPException(status_code=404, detail="Movie not found! Check ID and try again")
```

## 📤 Error Output
```python
    ^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/fastapi/routing.py", line 212, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/main.py", line 100, in get_single_movie
    raise HTTPException(status_code=404, message="Movie not found! Check ID and try again")
          ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: HTTPException.__init__() got an unexpected keyword argument 'message'
```

## ✅ Solution
```diff
-   raise HTTPException(status_code=404, message="Movie not found! Check ID and try again")
+   raise HTTPException(status_code=404, detail="Movie not found! Check ID and try again")
```

---
# ERROR: 14

## 📥 Input Code
```python
@app.put('/update-movie', status_code=200)
async def update_movie(movies: MovieRequest):
    for i in range(len(movies_db)):
        print(f'{movies.id=}');
        if movies.id == movies_db[i].id:
            movies_db[i] = movies 
                # do something
```

## 📤 Error Output
```python
INFO:     127.0.0.1:47992 - "GET /movies?offset=0&limit=10 HTTP/1.1" 200 OK
movie.id=UUID('8cb25c58-563c-4d53-97c4-e0379da5933d')
movie.id=UUID('8cb25c58-563c-4d53-97c4-e0379da5933d')
movie.id=UUID('8cb25c58-563c-4d53-97c4-e0379da5933d')
movie.id=UUID('8cb25c58-563c-4d53-97c4-e0379da5933d')
```

## ✅ Solution
```diff
@app.put('/update-movie', status_code=200)
async def update_movie(movies: MovieRequest):
    for i in range(len(movies_db)):
+       if str(movies.id) == movies_db[i].id:
-       if movies.id == movies_db[i].id:
            movies_db[i] = movies 
                # do something
```

## 📝 Analysis
**Root Cause:** 
> ALWAYS FUCKING STRINGIFY THE UUIDS since its return instance will never match to the inMEM DB


---
# ERROR: 15

## 📥 Input Code
```python
connect_my_db.execute(text('CREATE TABLE IF NOT EXISTS movie_ratings (id int, name str, description str, cast str, music_director str'))  
```

## 📤 Error Output
```python
❯ python db/db.py
Traceback (most recent call last):
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1961, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 944, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: incomplete input

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/db/db.py", line 11, in <module>
    connect_my_db.execute(text('CREATE TABLE movie_ratings (id uuid, name str, description str, cast str, music_director str, release_year date, created_at datetime, updated_at datetime'))
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1413, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/sql/elements.py", line 526, in _execute_on_connection
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1635, in _execute_clauseelement
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1840, in _execute_context
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1980, in _exec_single_context
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 2349, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/base.py", line 1961, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/engine/default.py", line 944, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) incomplete input
[SQL: CREATE TABLE movie_ratings (id uuid, name str, description str, cast str, music_director str, release_year date, created_at datetime, updated_at datetime]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
```

## ✅ Solution
```diff
-connect_my_db.execute(text('CREATE TABLE IF NOT EXISTS movie_ratings (id int, name str, description str, cast str, music_director str'))
+connect_my_db.execute(text('CREATE TABLE IF NOT EXISTS movie_ratings (id int, name str, description str, cast str, music_director str)'))
```

---

# ERROR: 16

## 📥 Input Code
```python
from sqlalchemy import Session
```

## 📤 Error Output
```python
Traceback (most recent call last):
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/db/db.py", line 21, in <module>
    from sqlalchemy import Session
ImportError: cannot import name 'Session' from 'sqlalchemy' (/mnt/e/e-drive/coding/newnew/py/fastAPI/items-app/.venv/lib/python3.13/site-packages/sqlalchemy/__init__.py)
```

## ✅ Solution
```diff
Traceback (most recent call last):
-   from sqlalchemy import Session
+   from sqlalchemy.orm import Session
```

---
# ERROR: 17

## 📥 Input Code
```python
None
```

## 📤 Error Output
```python
sqlalchemy.exc.ProgrammingError: (mysql.connector.errors.ProgrammingError) 1049 (42000): Unknown database 'testing_sqlalchemy_slaves'
(Background on this error at: https://sqlalche.me/e/20/f405)
```

## ✅ Solution
```diff
create the database manually using mysql cli
```
---
# ERROR: 18

## 📥 Input Code
```python
class MovieRating(DeclarativeBase):
    __tablename__ = 'movie_rating'
```

## 📤 Error Output
```python
sqlalchemy.exc.InvalidRequestError: Cannot use 'DeclarativeBase' directly as a declarative base class. Create a Base by creating a subclass of it.
```

## ✅ Solution
```diff
+class Base(DeclarativeBase):
     pass

-class MovieRating(DeclarativeBase):
+class MovieRating(Base):
     __tablename__ = 'movie_rating'
```
---
# ERROR: 19

## 📥 Input Code
```python
MovieRating.metadata.create_all(bind=engine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
```

## 📤 Error Output
```python
sqlalchemy.exc.ProgrammingError: (mysql.connector.errors.ProgrammingError) 1049 (42000): Unknown database 'SomeDBname'
(Background on this error at: https://sqlalche.me/e/20/f405)
```

## ✅ Solution
```diff
just create the database using mysql cli /gui 
```

---
# ERROR: 20

## 📥 Input Code
```python
code
```

## 📤 Error Output
```python
sqlalchemy.exc.CompileError: (in table 'movie_rating', column 'name'): VARCHAR requires a length on dialect mysql
```

## ✅ Solution
```diff
error
```


## 📝 Analysis
**Root Cause:** 
i had to give length of string/varchar. eg: string(20)

---
# ERROR: 21

## 📥 Input Code
```python
NA
```

## 📤 Error Output
```python
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
```

## ✅ Solution
```diff
in url, use `http://localhost...` instead of `https://localhost:`
```


## 🔗 Resources
- https://stackoverflow.com/questions/70726187/invalid-http-request-received-with-fast-api 

---
# ERROR: 22

## 📥 Input Code
```python
NA
MYSQL_CONN_URL='mysql+mysqlconnector://root:nigger@localhost/alchemy_bhosadika'
```

## 📤 Error Output
```python
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/testing-knowledge/.venv/lib/python3.13/site-packages/sqlalchemy/dialects/mysql/mysqldb.py", line 167, in import_dbapi
    return __import__("MySQLdb")
ModuleNotFoundError: No module named 'MySQLdb'
```

## ✅ Solution
```diff
+MYSQL_CONN_URL='mysql+mysqlconnector://root:nigger@localhost/alchemy_bhosadika'
-MYSQL_CONN_URL='mysql://root:nigger@localhost/alchemy_bhosadika'
```

---
# ERROR: 23

## 📥 Input Code
```python
uv add python-dotenv
```

## 📤 Error Output
```python
❯ uv add python-dotenv
⠹ testing-knowledge==0.1.0                                                                   error: Failed to fetch: `https://pypi.org/simple/uvicorn/`
  Caused by: Request failed after 3 retries
  Caused by: error sending request for url (https://pypi.org/simple/uvicorn/)
  Caused by: operation timed out
```

## ✅ Solution
```diff
LITERALLY TURN OF CLOUDFLARE WARP :LOL:
```

## 🔗 Resources
- https://stackoverflow.com/questions/57648998/connection-to-pypi-org-timed-out

---
# ERROR: 24

## 📥 Input Code
```python
    cast = Column(ARRAY(String(20))) 
```

## 📤 Error Output
```python
sqlalchemy.exc.CompileError: (in table 'movie_rating', column 'cast'): Compiler <sqlalchemy.dialects.mysql.base.MySQLTypeCompiler object at 0x7142b7b80590> can't render element of type ARRAY
```

## ✅ Solution
```diff
mysql cant handle arrays. have to use different table
```


---
# ERROR: 25

## 📥 Input Code
```python
# enum
class Gender(str, Enum):
    male= "Male"
    female = "Female"

# enum
class Role(str, Enum): 
    guest = "Guest"
    moderator = "Moderator"
    admin =  "Admin"

class UserRequest(BaseModel):
    first_name : str 
    last_name : str 
    email : str 
    password : str 
    role : str = Field(default=Role)
    gender: str = Field(default=Gender)
    created_at : datetime
```

## 📤 Error Output
```python
sqlalchemy.exc.StatementError: (builtins.TypeError) unhashable type: 'list'
[SQL: INSERT INTO users (first_name, last_name, email, password, `role`, gender, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(role)s, %(gender)s, %(created_at)s)]
[parameters: [{'created_at': datetime.datetime(2025, 9, 16, 14, 59, 7, 951000, tzinfo=TzInfo(UTC)), 'password': 'string', 'gender': [<Gender.male: 'Male'>], 'role': [<Role.guest: 'Guest'>], 'last_name': 'testing', 'email': 'test@hotmail.com', 'first_name': 'somename'}]]
```

## ✅ Solution
```diff
class UserRequest(BaseModel):
    first_name : str 
    last_name : str 
    email : str 
    password : str 
-   role : str = Field(default=Role)
+   role : Role = Role.guest
-   gender: str = Field(default=Gender)
+   gender: Gender = Gender.male 
    created_at : datetime
```

## 📝 Analysis
**Root Cause:** 
db tried to take only one value in field. i tried to shove a list and not set a default value from the enums

## 🔗 Resources
- gemini 



---
# ERROR: 26

## 📥 Input Code
```python
    email, password = user_req['email'], [ 'password']

```

## 📤 Error Output
```python
    email, password = user_req['email'], [ 'password']
                      ~~~~~~~~^^^^^^^^^
TypeError: 'UserRequest' object is not subscriptable
```

## ✅ Solution
```diff
error
```
fix

## 📝 Analysis
**Root Cause:** 
description

## 🔗 Resources
- N/A


---
# ERROR: 27

## 📥 Input Code
```python
passlib library i think
```

## 📤 Error Output
```python
Traceback (most recent call last):
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/Movies-API/.venv/lib/python3.13/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_backend_mixin
    version = _bcrypt.__about__.__version__
              ^^^^^^^^^^^^^^^^^
AttributeError: module 'bcrypt' has no attribute '__about__'
```

## ✅ Solution
```diff
error
```
fix

## 📝 Analysis
**Root Cause:** 
description

## 🔗 Resources
- N/A


---
# ERROR: 28

## 📥 Input Code
```python
def sign_up(user_req: UserRequest,  db: db_inject):
-   user_body = UserRequest(
        first_name=user_req.first_name,
        last_name=user_req.last_name,
```

## 📤 Error Output
```python
    db.add(user_body)
    ~~~~~~^^^^^^^^^^^
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/Movies-API/.venv/lib/python3.13/site-packages/sqlalchemy/orm/session.py", line 3479, in add
    raise exc.UnmappedInstanceError(instance) from err
sqlalchemy.orm.exc.UnmappedInstanceError: Class 'routers.auth.UserRequest' is not mapped
```

## ✅ Solution
```diff
def sign_up(user_req: UserRequest,  db: db_inject):
-   user_body = UserRequest(
+   user_body = Users(
        first_name=user_req.first_name,
        last_name=user_req.last_name,
...

```

## 📝 Analysis
**Root Cause:** 
my dumass was trying to save it in a REQUEST CLASS!!! dumb dumb dumb. i had to only pass the incoming json values inside the User's Model that CAME from the REQUEST CLASS. NOT THE REQUEST CLASS! 

## 🔗 Resources
- N/A


---

---
# ERROR: 29

## 📥 Input Code
```python
NA
```

## 📤 Error Output
```python
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/Movies-API/utils/gen_access_tkn.py", line 2, in <module>
    from jose import jwt
  File "/mnt/e/e-drive/coding/newnew/py/fastAPI/Movies-API/.venv/lib/python3.13/site-packages/jose.py", line 546
    print decrypt(deserialize_compact(jwt), {'k':key},
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

## ✅ Solution
```diff
DONT USE JOSE[CRYPTOGRAPHY] lib. use the `pyjwt lib for jwt (best and similar) 
```
---


---
# ERROR: 30

## 📥 Input Code
```python
code
```

## 📤 Error Output
```python
_mysql_connector.MySQLInterfaceError: Access denied for user 'root'@'localhost' (using password: YES)

sqlalchemy.exc.ProgrammingError: (mysql.connector.errors.ProgrammingError) 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

## ✅ Solution
```diff

```

## 📝 Analysis
description

## 🔗 Resources
- N/A