[[CSS Selector]]
In XPath, there are seven kinds of nodes: element, attribute, text, namespace, processing-instruction, comment, and document nodes.
## Relationship of Nodes
### Parent
Each element and attribute has one parent.
In the following example; the book element is the parent of the title, author, year, and price:

```
<book>  
  <title>Harry Potter</title>  
  <author>J K. Rowling</author>  
  <year>2005</year>  
  <price>29.99</price>  
</book>
```

### Children
Element nodes may have zero, one or more children.
In the following example; the title, author, year, and price elements are all children of the book element:
```
<book>  
  <title>Harry Potter</title>  
  <author>J K. Rowling</author>  
  <year>2005</year>  
  <price>29.99</price>  
</book>
```

### Siblings
Nodes that have the same parent.
In the following example; the title, author, year, and price elements are all siblings:
```
<book>  
  <title>Harry Potter</title>  
  <author>J K. Rowling</author>  
  <year>2005</year>  
  <price>29.99</price>  
</book>
```

## Selecting Nodes
| **Expression** | **Description** }                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| _nodename_     | Selects all nodes with the name "_nodename_"                                                          |
| /              | Selects from the root node                                                                            |
| //             | Selects nodes in the document from the current node that match the selection no matter where they are |
| .              | Selects the current node                                                                              |
| ..             | Selects the parent of the current node                                                                |
| @              | Selects attributes                                                                                    | 
Example
![](https://s2.loli.net/2022/05/21/XYHMVQBwLnbNPK8.png)
