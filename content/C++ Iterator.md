---
aliases: []
tags: []
date created: Apr 9th, 2022
date modified: Dec 24th, 2022
---
Used in [[C++ STL]]  
[Source](https://docs.microsoft.com/en-us/cpp/standard-library/iterators?view=msvc-170)

## What
An iterator is an **object** (like a [[pointer]]) that points to an element inside the container.  
The [[C++]] Standard Library containers all provide iterators so that algorithms can access their elements in a standard way without having to be concerned with the type of container the elements are stored in.  
You can use iterators explicitly using member and global functions such as `begin()` and `end()` and operators such as `++` and `--` to move forward or backward. You can also use iterators implicitly with a range-for loop or (for some iterator types) the subscript operator `[]`.

```c++
vector<int> vec{ 0,1,2,3,4 };
for (auto it = begin(vec); it != end(vec); it++)
{
    // Access element using dereference operator
    cout << *it << " ";
}
```

There are five categories of iterators. In order of increasing power, the categories are:
- **Output**. An _output iterator_ `X` can iterate forward over a sequence by using the `++` operator, and can write an element only once, by using the **`*`** operator.
- **Input**. An _input iterator_ `X` can iterate forward over a sequence by using the `++` operator, and can read an element any number of times by using the `*` operator. You can compare input iterators by using the `==` and `!=` operators. After you increment any copy of an input iterator, none of the other copies can safely be compared, dereferenced, or incremented afterwards.
- **Forward**. A _forward iterator_ `X` can iterate forward over a sequence using the ++ operator and can read any element or write non-const elements any number of times by using the `*` operator. You can access element members by using the `->` operator and compare forward iterators by using the `==` and `!=` operators. You can make multiple copies of a forward iterator, each of which can be dereferenced and incremented independently. A forward iterator that is initialized without reference to any container is called a _null forward iterator_. Null forward iterators always compare equal.
- **Bidirectional**. A _bidirectional iterator_ `X` can take the place of a forward iterator. You can, however, also decrement a bidirectional iterator, as in `--X`, `X--`, or `(V = *X--)`. You can access element members and compare bidirectional iterators in the same way as forward iterators.
- **Random access**. A _random-access iterator_ `X` can take the place of a bidirectional iterator. With a random access iterator, you can use the subscript operator `[]` to access elements. You can use the `+`, `-`, `+=` and `-=` operators to move forward or backward a specified number of elements and to calculate the distance between iterators. You can compare bidirectional iterators by using `==`, `!=`, `<`, `>`, `<=`, and `>=`.

## How to Use
- [Iterators in C++ STL - GeeksforGeeks](https://www.geeksforgeeks.org/iterators-c-stl/)
1. **`begin()`**: The begin() function is a member function of the C++ containers such as vector, list, etc., that returns an iterator pointing to the first element in the container. 
2. **`end()`**: Member function of the C++ Iterator class which returns an iterator pointing to the past-the-end element of a container. It compares equal to the result of the last incrementing operator for any valid iterator range in this container. If the container is empty, then `end()` points to the same position as `begin()`.  
3. **`advance()`** : `advance()` is a method used to increment an iterator given the number of elements it should be advanced by. It takes distance as argument and returns nothing. It's defined in the `<iterator>` header.
4. **`next()`**: The `next()` method returns the next element in the sequence.
5. **`prev()`**: Opposite of `next()`
6. **`inserter()`**: It takes a container and an iterator as arguments and returns an iterator that can be used to insert elements into the container. The returned iterator is an `insert_iterator`, which allows elements to be inserted into the container using `operator*` and `operator++`. This is useful for cases where elements need to be inserted into a particular position in the container, such as when merging two sorted lists.