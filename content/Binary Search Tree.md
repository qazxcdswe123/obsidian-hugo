---
aliases: [BST]
date created: Nov 1st, 2022
date modified: Nov 2nd, 2022
---
[[Tree]]
[Example](https://github.com/qazxcdswe123/DeathRoadToBaldness/blob/main/100.Ketangpai/013_bst.cpp)

## Deletion (By Value) or Change Value in BST
关键：递归，缩小子树。 (Top Down) 
删除的是 successor 而不是 target，之后换值，保留其搜索性质，删除 leaf node.  
每次递归时修改递归方向的节点为函数返回值，达到命中的节点修改，没命中的节点不变的效果（末尾返回 root）不更改中间节点。  
Base Case 有两种，一种是没找到 Key，不做修改 （ return root ）；一种是找到了，分三种情况。
- 左节点为空 - 连接右节点
- 右节点为空 - 连接左节点
- 含 key 的节点为 root ，有两个子节点，找和它最接近的值（右的最左或左的最右 | successor），修改 root 的值为 successor 的值，删除 successor

```c++
node *deleteNodeByKey(node *root, int key)
{
    if (root == NULL)
        return root;
    if (root->data < key)
        root->right = deleteNodeByKey(root->right, key);
    else if (root->data > key)
        root->left = deleteNodeByKey(root->left, key);
    else
    {
        if (root->left == NULL)
        {
            node *temp = root->right;
            delete root;
            return temp;
        }
        else if (root->right == NULL)
        {
            node *temp = root->left;
            delete root;
            return temp;
        }

        // 此时的 root->data == key, 并且存在子节点

        // 找到其 successor
        node *temp = minValue(root->right);
        // root 的值替换成 successor 的值，完成值上的替换
        root->data = temp->data;
        // 删除 successor
        root->right = deleteNodeByKey(root->right, temp->data);
    }
    return root;
}
```
