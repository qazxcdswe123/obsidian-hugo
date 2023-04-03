---
aliases: []
date created: Jun 28th, 2022
date modified: Nov 7th, 2022
---
[https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp)
- Text Type
	- `str`
- Numeric Types
	- `int`, `float`, `complex`
	- complex 复数

	```python
	a = complex(1) # Passing single parameter 
	b = complex(1,2) # Passing both parameters

	(1+0j)
	(1+2j)
	```

- Sequence Types
	- `list`, `tuple`, `range`, `set`
- Mapping Type
	- `dict`
- Slice: 左闭右开

# Set
`myset = {"apple", "banana", "cherry"}`  
`myset.add(word)`  
All elements are unique  
A set is a collection which is _unordered_, __unchangeable__, and _unindexed_.  
**Note:** Set _items_ are unchangeable, but you can remove items and add new items.  
`newtup = tuple(set(tup)–{'PYTHON'}) # 去重同时删除数据项`

# List
[[Python List]]

# Tuple
Elements can't be changed
- `len`
- `max`
- `min`
- `tuple(seq)`

# Dictionary
`**args`

```python
people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

name = get_string("Name: ")
if name in people:
    number = people[name] # index by first map
    print(f"Number: {number}")

my_dict = {"Name":[],"Address":[],"Age":[]};

my_dict["Name"].append("Guru")
my_dict["Address"].append("Mumbai")
my_dict["Age"].append(30)	
print(my_dict)
{'Name': ['Guru'], 'Address': ['Mumbai'], 'Age': [30]}

```

![](https://s2.loli.net/2022/06/28/t9zS8buQBcHmpyv.png)


# String
[[Python String]]
