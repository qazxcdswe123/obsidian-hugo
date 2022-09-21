---
aliases: []
tags: []
date created: Sep 20th, 2022
date modified: Sep 20th, 2022
---
[collections — Container datatypes — Python 3.10.7 documentation](https://docs.python.org/3/library/collections.html)

| Name                                                                                                                 | Description                                                      |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") | factory function for creating tuple subclasses with named fields |
| [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque")                  | list-like container with fast appends and pops on either end     |
| [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap "collections.ChainMap")         | dict-like class for creating a single view of multiple mappings  |
| ...                                                                                                                  | ...                                                              |

## Namedtuple
Returns a new tuple subclass named _typename_. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable.