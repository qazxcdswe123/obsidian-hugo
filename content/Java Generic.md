---
aliases: []
tags: []
date created: Feb 23rd, 2023
date modified: Mar 22nd, 2023
---

# Comparable
- [Comparable (Java Platform SE 8 )](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html)  

The most commonly used type parameter names are:
- E - Element (used extensively by the Java Collections Framework)
- K - Key
- N - Number
- T - Type
- V - Value
- S,U,V etc. - 2nd, 3rd, 4th types

# Optional
- Creating an Optional object:   
	- To create an Optional object with a non-null value, use the static method `Optional.of(T value)`.   
	- To create an Optional object that may or may not contain a null value, use the static method `Optional.ofNullable(T value)`
 - Retrieving the value from an Optional object:
	- To retrieve the value from an Optional object, use the method `get()`. This will throw a `NoSuchElementException` if the Optional is empty.
	- To retrieve the value from an Optional object or return a default value if it is empty, use the method `orElse(T other)`
 - Checking if an Optional object contains a non-null value:
	- To check if an Optional object contains a non-null value, use the method `isPresent()`. This returns true if there is a non-null value and false otherwise