---
aliases: []
tags: []
date created: May 29th, 2022
date modified: Mar 25th, 2023
---
- [[Python Namespace]]

## Class Object
`x = MyClass()`  
creates a new _instance_ of the class and assigns this object to the local variable `x`.

### Init
```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## Inheritance
`class DerivedClassName(modname.BaseClassName):`  
Python has two built-in functions that work with inheritance:
- Use [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") to check an instance’s type: `isinstance(obj, int)` will be `True` only if `obj.__class__` is [`int`](https://docs.python.org/3/library/functions.html#int "int") or some class derived from [`int`](https://docs.python.org/3/library/functions.html#int "int").
- Use [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") to check class inheritance: `issubclass(bool, int)` is `True` since [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") is a subclass of [`int`](https://docs.python.org/3/library/functions.html#int "int"). However, `issubclass(float, int)` is `False` since [`float`](https://docs.python.org/3/library/functions.html#float "float") is not a subclass of [`int`](https://docs.python.org/3/library/functions.html#int "int").

### Multiple Inheritance
`class DerivedClassName(Base1, Base2, Base3):`  
For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.  
Thus, if an attribute is not found in `DerivedClassName`, it is searched for in `Base1`, then (recursively) in the base classes of `Base1`, and if it was not found there, it was searched for in `Base2`, and so on.

## Private Variables
Any identifier of the form `__spam` (at least two leading underscores, at most one trailing underscore) is textually replaced with `_classname__spam`, where `classname` is the current class name with leading underscore(s) stripped.  
This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```