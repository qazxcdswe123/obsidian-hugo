---
aliases: []
tags: []
date created: Jun 19th, 2022
date modified: Sep 7th, 2022
---
[Src](https://www.geeksforgeeks.org/templates-cpp/)  
[ntu](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/cp8_Template.html)

# How it Works
Templates are expanded at compiler time. This is like macros. The difference is, that the compiler does type checking before template expansion. The idea is simple, source code contains only function/class, but compiled code may contain multiple copies of the same function/class.

# Function Template
A _function template_ is a generic function that is defined on a generic type for which a specific type can be substituted. Compiler will generate a function for each specific type used. Because types are used in the function parameters, they are also called _parameterized types_.

```c++
#include <iostream>
using namespace std;
 
// One function works for all data types.  This would work
// even for user defined types if operator '>' is overloaded
template <typename T>
T myMax(T x, T y)
{
   return (x > y) ? x: y;
}
 
int main()
{
  cout << myMax<int>(3, 7) << endl;  // Call myMax for int
  cout << myMax<double>(3.0, 7.0) << endl; // call myMax for double
  cout << myMax<char>('g', 'e') << endl;   // call myMax for char
 
  return 0;
}
```

##### More Than One Type Parameters
To use more than one type parameters in a template:

```cpp
template <typename T1, typename T2, ....>
class ClassName { ...... }
```

##### Default Type
You can also provide default type in template. For example,

```cpp
template <typename T = int>
class ClassName { ...... }
```

To instantiate with the default type, use `ClassName<>`.

##### Specialization

```cpp
// General Template
template <typename T>
class Complex { ...... }
 
// Specialization for type double
template <>
class Complex<double> { ...... }
 
// Specialization for type int
template <>
class Complex<int> { ....... }
```

# Class Template

```c++
#include <iostream>
using namespace std;

template <typename T>
class Array {
private:
	T *ptr;
	int size;
public:
	Array(T arr[], int s);
	void print();
};

template <typename T>
Array<T>::Array(T arr[], int s) {
	ptr = new T[s];
	size = s;
	for(int i = 0; i < size; i++)
		ptr[i] = arr[i];
}

template <typename T>
void Array<T>::print() {
	for (int i = 0; i < size; i++)
		cout<<" "<<*(ptr + i);
	cout<<endl;
}

int main() {
	int arr[5] = {1, 2, 3, 4, 5};
	Array<int> a(arr, 5);
	a.print();
	return 0;
}
```

**What is the difference between function overloading and templates?**  
Both function overloading and templates are examples of **polymorphism** feature of OOP. Function overloading is used when multiple functions do similar operations, templates are used when multiple functions do identical operations.
