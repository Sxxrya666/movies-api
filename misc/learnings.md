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



