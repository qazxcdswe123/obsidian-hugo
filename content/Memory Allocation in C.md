内存由两部分构成 [[Memory]]，和数据结构中的 [[Heap Data Structure]], [[Stack Data Structure]] 区分
# C/C++
## Malloc and Calloc
| Malloc                | Calloc                       |
| --------------------- | ---------------------------- |
| Wont initialize value | Will initialize value (to 0) |
| Faster                | Slower                       |

## Malloc vs New
| Malloc                | New              |
| --------------------- | ---------------- |
| On heap               | On heap          |
| Dont call constructor | Call Constructor |
___

## Free vs Delete
| Free                              | Delete          |
| --------------------------------- | --------------- |
| frees memory dont call destructor | Call destructor | 

[[C++ OOP]]