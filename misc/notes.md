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

- 