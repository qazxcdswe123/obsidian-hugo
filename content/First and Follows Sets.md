---
aliases: []
link: []
date created: Oct 29th, 2023
date modified: Oct 30th, 2023
---
- ﻿Consider non-terminal `A`, production `A -> a`, & token `t`

## First(a)
The idea behind `FIRST(a)` is to be able to predict what kind of production to use when parsing an input string. Knowing the set of terminals that can appear first in strings derived from `a` allows the parser to decide what to do when it encounters a particular symbol in the input.

- If `a ->* tb`
	- `a` can derive a `t` in the first position
	- `t` is a terminal
	- then $t \in First(a)$

![image.png](https://img.ynchen.me/2023/10/995adcac5d96d4ed3a7faed055272073.webp)

## Follow(a)
- If `A -> a`, `a ->* ep`, `S ->* b A t sig`
	- ﻿Useful if stack has `A`, input is `t`, and `A` cannot derive `t`
	- `a` can't derive `t`, we need to erase `a` so it must go to `ep`
	- `t` must come immediately after `A`, so we can get rid of `A` and match `t`
	- We say $t \in Follow(A)$  
 ![image.png](https://img.ynchen.me/2023/10/5b98204b69a5ea0346e49b3f30906912.webp)
 
 ![image.png](https://img.ynchen.me/2023/10/228a6f1bd904304bb36f5628ce9c147b.webp)
 

## Links
- [[Parsing]]