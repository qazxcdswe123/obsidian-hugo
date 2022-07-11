[[Python File]]

# String Datatype
`r` before string means **raw string**, won't be parsed.
```python
print(r'C:\some\name')  # note the r before the quote
C:\some\name
```
Two or more string literals = concatenated
```python
'Py' 'thon'
'Python'
text = ('Put several strings within parentheses '
...         'to have them joined together.')
'Put several strings within parentheses to have them joined together.'
```

## Documentation Strings
[Src](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
```python
>>> def my_function():
...     """Do nothing, but document it.
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

# String Manipulation
## str.join()
```python
delimiter = ","
csv_str = delimiter.join(['a', 'b', 'c'])
print(csv_str)  
# a,b,c

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
print(' '.join(text))
# Output: Python is a fun programming language
```

## repr() and str()
When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") or [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") functions.

The [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") function is meant to return representations of values which are fairly human-readable, while [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") is meant to generate representations which can be read by the interpreter (or will force a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") if there is no equivalent syntax).
```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

## format string
- fstring
```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```
-  `str.format()`
```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```
Other modifiers can be used to convert the value before it is formatted. `'!a'` applies [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii"), `'!s'` applies [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"), and `'!r'` applies [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"):
```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
- `str.strip()` 
remove match
```python
txt = ",,,,,rrttgg.....banana....rrr"  
x = txt.strip(",.grt")  
print(x)
banana
```


# F-string
Formatted string literals (also called _f_-_strings_ for short)
## Alignment
**Approach :** The syntax of the alignment of the output string is defined by `<`, `>`, `^` and followed by the width number
**Example 1 :** For Left Alignment output string syntax define ‘<‘ followed by the width number.
`print(f"{'Left Aligned Text' : <20}")`
**Example 2 :** For Right Alignment output string syntax define ‘>’ followed by the width number.
`print(f"{'Right Aligned Text' : >20}")`
**Example 3 :** For Center Alignment output string syntax define ‘^’ followed by the width number.
`print(f"{'Centered' : ^10}")`