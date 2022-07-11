[Copy constructor](https://www.geeksforgeeks.org/shallow-copy-and-deep-copy-in-c/)
Creating a copy of object by copying data of all member variables as it is, is called **shallow copy** 
while creating an object by copying data of another object along with the values of memory resources resides outside the object but handled by that object, is called **deep copy**.
# Shallow copy
In shallow copy, an object is created by simply copying the data of all variables of the original object.
This works well if none of the variables of the object are defined in the [heap section of memory](https://www.geeksforgeeks.org/stack-vs-heap-memory-allocation/). If some variables are dynamically allocated memory from heap section, then copied object variable will also reference then same memory location.
# Deep copy
In Deep copy, an object is created by copying data of all variables and it also allocates similar memory resources with the same value to the object.
