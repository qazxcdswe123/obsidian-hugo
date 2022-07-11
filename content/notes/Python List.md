[[Python Datatypes and Storage]]
# List Basis
`*args`
```python
scores = [72, 73, 33]

average = sum(scores) / len(scores)
print(f"Average: {average}")
```
The `f` before the double quotes indicates that this is a **format string**, which will allow us to use curly braces, `{}`, to include variables that should be substituted, or interpolated. [[Python f-string]]
___
It is possible to nest lists (create lists containing other lists), for example:
```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```
___
- List comprehension
`newlist = [x for x in fruits if x != "apple"]`

## List Comprehension
[Src](https://www.programiz.com/python-programming/list-comprehension)
[Python Docs](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
```python
h_letters = [ letter for letter in 'human' ]
print( h_letters)
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

squares = [x**2 for x in range(10)]
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

# More on Lists
[More On Lists]( https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- `list.append(x)` 
	- Add an item to the end of the list. Equivalent to `a[len(a):] = [x]`.
- `list.extend(iterable)`
	- Extend the list by appending all the items from the iterable. Equivalent to `a[len(a):] = iterable`.
- `list.insert(i, x)`
	- Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.
- `list.remove(x)`
	- Remove the first item from the list whose value is equal to _x_. It raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if there is no such item.
- `list.pop([i])`
	- Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list.
	- The square brackets around the _i_ in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.
- `list.clear()`
	- Remove all items from the list. Equivalent to `del a[:]`.
- `list.index(x[, start[, end]])`
	- Return zero-based index in the list of the first item whose value is equal to _x_. Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if there is no such item.
	- The optional arguments _start_ and _end_ are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the _start_ argument.
- `list.count(x)`
	- Return the number of times _x_ appears in the list.
- `list.sort(*, key=None, reverse=False)`
	- Sort the items of the list in place (the arguments can be used for sort customization, see [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted") for their explanation).
- `list.reverse()`
	- Reverse the elements of the list in place.
- `list.copy()`
	- Return a shallow copy of the list. Equivalent to `a[:]`.

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
