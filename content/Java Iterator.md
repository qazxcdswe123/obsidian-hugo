## `Methods`
- `boolean hasNext()`
	- Returns true if there are more elements. Otherwise, returns false.
- `Object next()`
	- Returns the next element. Throws `NoSuchElementException` if there is not a next element.
- `void remove()`
	- Removes the current element. Throws `IllegalStateException` if an attempt is made to call `remove()` that is not preceded by a call to `next()`.

## Links
- [[C++ Iterator]]
- [[Rust Iterator]]
- [Java - How to Use Iterator?](https://www.tutorialspoint.com/java/java_using_iterator.htm)