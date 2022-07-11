# Match
```python
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _: # wild card
            print("Not a point")
```

-   Most literals are compared by equality, however the singletons `True`, `False` and `None` are compared by identity.