---
title: C++ Deque
---
- Deque
```cpp
#include <deque>
using std::deque;

deque<int> deq; // 定义一个int类型的双端队列a
deque<int> deq(10); // 定义一个int类型的双端队列a，并设置初始大小为10
deque<int> deq(10, 1); // 定义一个int类型的双端队列a，并设置初始大小为10且初始值都为1

int n[] = { 1, 2, 3, 4, 5 };
deque<int> a(n, n + 5); 

int size = deq.size();
bool isEmpty = deq.empty();

deq.push_front(4);
deq.push_back(5);

deque<int>::iterator it = deq.begin();
deq.insert(it, 2);

deq.pop_front();
deq.pop_back();

int front = deq.front();
int back = deq.back();
```