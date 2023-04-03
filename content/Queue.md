---
aliases: [队列]
date created: Jul 8th, 2022
date modified: Aug 19th, 2022
---
#Data-structure 
# Queue
Similar with [[Stack Data Structure]]  
FIFO

```cpp
#include <bits/stdc++.h>
using namespace std;

class QueueNode
{
public:
    int data;
    QueueNode *next;
};

class Queue
{
public:
    QueueNode *front, *rear;
};

QueueNode *newNode(int data)
{
    QueueNode *Node = new QueueNode();
    Node->data = data;
    Node->next = nullptr;
    return Node;
}

Queue *createQueue()
{
    Queue *q = new Queue();
    q->front = q->rear = nullptr;
    return q;
}

void enQueue(Queue *q, int data)
{
    QueueNode *temp = newNode(data);

    if (q->rear == nullptr)
    {
        cout << data << " enqueued\n";
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
    cout << data << " enqueued\n";
}

QueueNode *deQueue(Queue *q)
{
    if (q->front == nullptr)
    {
        return NULL;
    }

    QueueNode *temp = q->front;
    q->front = q->front->next;
    int data = temp->data;
    cout << data << " dequeued\n";

    // If front becomes NULL, then
    // change rear also as NULL
    if (q->front == nullptr)
    {
        q->rear = nullptr;
    }
    return temp;
}

int main()
{
    Queue *q = createQueue();
    enQueue(q, 10);
    enQueue(q, 20);
    deQueue(q);
    deQueue(q);
    enQueue(q, 30);
    enQueue(q, 40);
    enQueue(q, 50);
    QueueNode *n = deQueue(q);
    if (n != NULL)
    {
        cout << "Dequeued item is " << n->data << "\n";
    }
}
```

# Priority Queue


[[Sorting Algorithm]]
