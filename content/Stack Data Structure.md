#Data-structure 
Similar with: [[Queue]], but `LIFO`

```cpp
#include <bits/stdc++.h>
using namespace std;

class StackNode
{
public:
    int data;
    StackNode *next;
};

StackNode *newNode(int data)
{
    StackNode *Node = new StackNode();
    Node->data = data;
    Node->next = nullptr;
    return Node;
}

bool isEmpty(StackNode *root)
{
    return root == nullptr;
}

void push(StackNode **root, int data)
{
    StackNode *nNode = newNode(data);
    nNode->next = *root;
    *root = nNode;
    cout << data << " pushed to stack\n";
}

int pop(StackNode **root)
{
    if (isEmpty(*root))
    {
        return -1;
    }
    StackNode *temp = *root;
    *root = (*root)->next;
    int data = temp->data;
    delete temp;
    return data;
}

int peek(StackNode *root)
{
    if (isEmpty(root))
    {
        return -1;
    }

    return root->data;
}

int main()
{
    StackNode *root = nullptr;
    push(&root, 10);
    push(&root, 20);
    push(&root, 40);
    cout << "Top element is " << peek(root) << endl;

    while (!isEmpty(root))
    {
        cout << peek(root) << " ";
        pop(&root);
    }
}
```