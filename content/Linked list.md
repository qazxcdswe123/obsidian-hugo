---
aliases: []
tags: []
date created: Jul 24th, 2022
date modified: Aug 15th, 2022
---
- -> 其实是 (\*pointer).value
- [[C]] 中有 [[C++ STL]] ，效果几乎相同，效率和数组相似
- Error handling using new

```cpp
char* c = new (std::nothrow) char[100];
if (!c) {
// Handle error
}
```

- Deque 效果和 Doubly Linked List 完全相同
---
注意内存泄漏  
全部用函数管理会好一些

```cpp
void insert_front(struct Node** head, int new_data) // **指向指针的指针
{
   //allocate memory for New node
   struct Node* newNode = new Node;

   //assign data to new node
   newNode->data = new_data;

   //new node is head and previous is null, since we are adding at the front
   newNode->next = (*head);
   newNode->prev = NULL;

   //previous of head is new node
   if ((*head) != NULL)
   (*head)->prev = newNode;

   //head points to new node
   (*head) = newNode;
}

// insert after
void insert_After(struct Node* prev_node, int new_data)
{
   //check if prev node is null
   if (prev_node == NULL) {
   cout<<"Previous node is required , it cannot be NULL";
   return;
}
   //allocate memory for new node
   struct Node* newNode = new Node;

   //assign data to new node
   newNode->data = new_data;

   //set next of newnode to next of prev node
   newNode->next = prev_node->next;

   //set next of prev node to newnode
   prev_node->next = newNode;

   //now set prev of newnode to prev node
   newNode->prev = prev_node;

   //set prev of new node's next to newnode
   if (newNode->next != NULL)
   newNode->next->prev = newNode;
}
```

可用于实现大部分 #Data-structure , 如 [[Binary Search Tree]] [[Queue]] [[Stack Data Structure]] [[Heap data structure]]

