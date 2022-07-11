[pdb docs](https://docs.python.org/3/library/pdb.html)
assert 
# Try-catch
```python
try:
    x = int(input("x: "))
except ValueError:
    print("That is not an int!)
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!)
    exit()
print(x + y)
```
