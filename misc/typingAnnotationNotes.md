## Syntaxes
- `type` <variableName>= <define some types here>
- `Optional[<some_data_type>] 
- `NewType(<give_some_name>, <actual_type_definition_here>)
- `TypedDict` will hlep to individually mark types for each VARIABLE. it will help prevent unintended type castings for any vals. WILL BE INHERITED IN CLASS
- `Any` is used when i dont know what type of data will be in input and output. [but for IDE it will not be helpful if i want to access anything like methods or shit if a func is stored in a var]
- `TypeVar()`: `Any` ka better alternative. it will solve the above point's problem + it can be used for unknown types"
## syntax: 
```python
def some_func[T](arg1: T) -> T:
    pass
```

> in plain english: *"this is a func where this [T] thing will be defined as TypeVar, which will take arg1 as argument with type T, WHICH WILL RETURN THE **SAME** TYPE"*

- Focus on this pattern: `Annotated[<TYPE>, <METADATA>]`

-   `<TYPE>` is the normal type hint (`int`, `str`, `bool`).
    
-   `<METADATA>` is the "sticky note" for other tools.




---
- uv add this lib `types-request`  