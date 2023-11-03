---
aliases:
  - CFG
link:
  - "[[Backus-Naur Form]]"
date created: Oct 7th, 2023
date modified: Oct 29th, 2023
---
- $(V, \Sigma, R, S)$
	- V is the set of variables, or **nonterminals**.
		- Typically in **upper case**
	- Σ is the set of **terminal** symbols.
		- Typically in **lower case**
	- R is the set of production rules.
	- S is the start symbol.
	- Example: $(V, \Sigma, R, S) = (\{S, N, T\}, \{a, b\}, \{S \to NT, T \to aT | b\}, S)$

| Palindrome | Derivation |  
|---|---|  
| abba | S ⇒ NT ⇒ aT ⇒ ab ⇒ abba |  
| aba | S ⇒ NT ⇒ aT ⇒ ab ⇒ aba |  
| b | S ⇒ NT ⇒ b ⇒ b |  
| aa | S ⇒ NT ⇒ aa |

- Derive
- Yields


## Links
- [[First and Follows Sets]]
- [[Parsing]]