---
aliases: []
tags: []
date created: Feb 22nd, 2023
date modified: Feb 22nd, 2023
---
A _collection_ is an object that groups multiple elements into a single unit. Collections are used to store, retrieve, manipulate, and communicate aggregate data.

# `Array`
An **array** is a dynamically-created object.  
Some other useful operations provided by methods in the `java.util.Arrays` class are:
- Searching an array for a specific value to get the index at which it is placed (the `binarySearch` method).
- Comparing two arrays to determine if they are equal or not (the `equals` method).
- Filling an array to place a specific value at each index (the `fill` method).
- Sorting an array into ascending order. This can be done either sequentially, using the `sort` method, or concurrently, using the `parallelSort` method introduced in Java SE 8. Parallel sorting of large arrays on multiprocessor systems is faster than sequential array sorting.
- Creating a stream that uses an array as its source (the `stream` method). For example, the following statement prints the contents of the `copyTo` array in the same way as in the previous example:  
	`java.util.Arrays.stream(copyTo).map(coffee -> coffee + " ").forEach(System.out::print);`  
    See [Aggregate Operations](https://docs.oracle.com/javase/tutorial/collections/streams/index.html) for more information about streams.
- Converting an array to a string. The `toString` method converts each element of the array to a string, separates them with commas, then surrounds them with brackets. For example, the following statement converts the `copyTo` array to a string and prints it:  
	`System.out.println(java.util.Arrays.toString(copyTo));`

# `ArrayList`
In Java, **ArrayList** is a class of Collections framework. It implements **`List<E>, Collection<E>, Iterable<E>`, Cloneable, Serializable**, and **RandomAccess** interfaces. It extends **`AbstractList<E>`** class.