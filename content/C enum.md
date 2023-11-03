---
link: []
aliases: []
date created: Mar 8th, 2022
date modified: Aug 1st, 2023
---
- [https://www.geeksforgeeks.org/enumeration-enum-c](https://www.geeksforgeeks.org/enumeration-enum-c/)  
- [https://www.programiz.com/c-programming/c-enumeration](https://www.programiz.com/c-programming/c-enumeration)  
- [https://en.cppreference.com/w/cpp/language/enum](https://en.cppreference.com/w/cpp/language/enum)

```cpp
enum enum_var{var0, var1, var2 = 22} outside_var;
enum week{Mon, Tue, Wed, Thur, Fri, Sat, Sun};

enum enum_var use_var;
enum week day;
day = Wed;
use_var = var0;
```

An enum variable can take only one value. The size of enum variable is a int.  
Can only output a int, use `if` or `case` to print the value.

## C++

### Named enum
```cpp
enum class CoordinateArea { FirstArea, SecondArea, ThirdArea, FourthArea};

CoordinateArea caOne = CoordinateArea::FirstArea;
CoordinateArea caSome= CoordinateArea::FourhtArea;
```