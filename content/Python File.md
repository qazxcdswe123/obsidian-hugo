# open()
[Src](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
[`open()`](https://docs.python.org/3/library/functions.html#open "open") returns a [file object](https://docs.python.org/3/glossary.html#term-file-object), and is most commonly used with two positional arguments and one keyword argument: `open(filename, mode, encoding=None)`

`f = open('workfile', 'w', encoding="utf-8")`
- The first argument is a string containing the filename.
- The second argument is another string containing a few characters describing the way in which the file will be used.
	- _mode_ can be `'r'` when the file will only be read
	- `'w'` for only writing (an existing file with the same name will be erased)
		- **It will delete the content first **
	- `'a'` opens the file for appending; any data written to the file is automatically **added to the end** (even when the file pointer is moved). 
	- `'r+'` opens the file for both reading and writing. The _mode_ argument is optional; `'r'` will be assumed if it’s omitted.
	- `a+` will create a file if not exist
- The file pointer is at the beginning of the file by default

## with
It is good practice to use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using `with` is also much shorter than writing equivalent [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)-[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) blocks:
```python
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

## write()
`f.write(string)` writes the contents of _string_ to the file, returning the number of characters written.
```python
>>> f.write('This is a test\n')
15

>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

## readline()
`f.readline()` reads a single line from the file; a newline character (`\n`) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline.
This makes the return value unambiguous; if `f.readline()` returns an empty string, the end of the file has been reached, while a blank line is represented by `'\n'`, a string containing only a single newline.
```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```
