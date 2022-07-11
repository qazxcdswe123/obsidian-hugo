![](https://s2.loli.net/2022/03/21/Lc4jV5OZUEBYaIk.png)
# with
We can use the `with` keyword, which will close the file for us after we’re finished:
```python
with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((name, number))
```
# pass
Another place [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass) can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The `pass` is silently ignored:
```python
def initlog(*args):
...     pass   # Remember to implement this!
```