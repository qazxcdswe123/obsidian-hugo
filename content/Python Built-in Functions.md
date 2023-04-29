---
aliases: []
date created: Jun 28th, 2022
date modified: Apr 27th, 2023
---

# print
```python
for i in range(4):
    print("?", end="")
print()
```

Default `end` is new line. Specify `end` to avoid `\n`
___

# chr ord
```python
x = ord('A') 
print(x)
y = chr(65) 
print(y)
output:
65
A

print(chr(ord('ć'))) 
print(ord(chr(65)))

output:
ć 
65
```

___

# sort() sorted()
sorted() can sort everything, return a list, won't change anything  
sort() sort immediately
___
Key can be the length, or the return value of a function, to be called on each list element **prior** to making comparisons. And [[Lambda and Anonymous Function]]  
here’s a case-insensitive string comparison:  
`sorted("This is a test string from Andrew".split(), key=str.lower)`  
A common pattern is to sort complex objects using some of the object’s indices as keys. For example:

```python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

___

# map
map() 是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

```python
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
[2, 4, 6, 8]

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
[2, 4, 6, 8]

l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
```

___

# zip
The `zip()` function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

```python
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result))

# Output: [('Java', 14), ('Python', 3), ('JavaScript', 6)]
```

___

# enumerate
index + content  
[Python Docs](https://docs.python.org/3/library/functions.html#enumerate)

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

___

# reversed() and sorted()
```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

___

# reduce
```python
from functools import reduce
print(functools.reduce(lambda a, b: a+b, lis))
```

---

# remove
remove via index  
已知 x = `[1, 2, 3, 2, 3]`,执行语句 x.remove(2) 之后,x = `[1, 3, 2, 3]`