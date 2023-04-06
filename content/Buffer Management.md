---
aliases: []
date created: Mar 19th, 2023
date modified: Mar 19th, 2023
---
![image.png](https://img.ynchen.me/2023/03/a46aa090f8d65265be322bc70fd5fa48.webp)

# Concurrency Module

## Buffer Manager
The table tracks 4 pieces of information: 
1. Frame ID that is uniquely associated with a memory address 
2. Page ID for determining which page a frame currently contains 
3. Dirty Bit for verifying whether or not a page has been modified
4. Pin Count for tracking the number of requestors currently using a page

- [[Replacement Policy]]

# Recovery Module

## Dirty Pages
- Dirty bit

## Links
- [[Page Table]]