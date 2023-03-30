---
aliases: []
tags: []
date created: Aug 15th, 2022
date modified: Aug 15th, 2022
---
- [[C++ STL]]
## `<stddef.h>`
The header `<stddef.h>` defines a type `ptrdiff_t` that is large enough to hold the signed difference of two pointer values.If we were being very cautious, however, we would use `size_t` for the return type of `strlen`, to match the standard library version. `size_t` is the unsigned integer type returned by the sizeof operator.)
[[size_t]]

## `<iomanip>`
`std::cout << std::setw(5) << std::setfill('0') << zipCode << std::endl`

## Files
[[C++ File]]  
In C++, files are mainly dealt by using three classes fstream, ifstream, ofstream available in `fstream` headerfile.  
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191129162746/CPP-File-Handling.png)