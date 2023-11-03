---
link:
  - "[[Backus-Naur Form]]"
aliases:
  - 有限自动机
date created: Jul 29th, 2023
date modified: Sep 26th, 2023
---

## DFA
$$
\begin{align*} & \text{Finite Automaton} = (Q, \Sigma, \delta, q_0, F) \\ & \text{where:} \\ & Q \text{ is a finite set of states} \\ & \Sigma \text{ is a finite set of symbols called the alphabet} \\ & \delta: Q \times \Sigma \rightarrow Q \text{ is the transition function} \\  
& q_0 \in Q \text{ is the start state} \\ & F \subseteq Q \text{ is the set of accept states} \end{align*}
$$

### Dense


### Sparse

## NFA
- multiple paths possible (0, 1 or many at each step)
- ε-transition is a “free” move without reading input
- Accept input if some path leads to accept state
- Useful Mathematically


## Conversion

### Regexp to NFA
- [[regex#Implementation]]
- Thompson Construction
	- [[Pikevm]]

### NFA to DFA
- subset construction
	- Epsilon Closure
### Minimize DFA
1. Divide the states into two sets. One contain all final states and other contain non-final states.
2. For every states in the two sets, if for every alphabet, the transition is not distinguishable, it can be joined.
- [Hopcroft's Paper](http://i.stanford.edu/pub/cstr/reports/cs/tr/71/190/CS-TR-71-190.pdf)

```
Partition ← { DA , { D – DA } }
Worklist ← { DA , { D – DA } }

while (Worklist ≠ ∅) do  
    select a set s from Worklist and remove it

    for each character c in alphabet do
	    Image ← { x | δ(x, c) ∈ s }
	
	    for each set q in Partition that has a state in Image do
	        q1 ← q ∩ Image  
	        q2 ← q – q1
	
	        if q2 ≠ ∅ then // split q around s and c 
		        remove q from Partition
	            Partition ← Partition ∪ q1 ∪ q2
	
		        if q is in Worklist then // and update the Worklist, remove q from Worklist  
		            Worklist ← Worklist ∪ q1 ∪ q2
		
		        else if |q1| ≤ |q2| then
		            Worklist ← Worklist ∪ q1
		
		        else
		            Worklist ← Worklist ∪ q2  
		
		        if s = q then // need another s
		            break
```

## Links
- [[Regular Expression]]