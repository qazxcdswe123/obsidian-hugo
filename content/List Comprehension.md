## Haskell
- [List comprehension - HaskellWiki](https://wiki.haskell.org/List_comprehension)

## Python
- [Python Docs](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

```python
h_letters = [ letter for letter in 'human' ]
print( h_letters)
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

squares = [x**2 for x in range(10)]
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```