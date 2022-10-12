---
aliases: []
tags: []
date created: Sep 27th, 2022
date modified: Sep 28th, 2022
---
# Loop
## For
The basic `for` loop has three components separated by semicolons:

- the init statement: executed before the first iteration
- the condition expression: evaluated before every iteration
- the post statement: executed at the end of every iteration

**Note:** Unlike other languages like C, Java, or JavaScript there are no parentheses surrounding the three components of the `for` statement and the braces `{ }` are always required.

```go
// for loop
for initialization; condition; post {
	// zero or more statements 
}

// while loop
for sum < 1000 {
		sum += sum
	}
```

## Range
`range` returns two values: the index of the current item in the loop, and a copy of the item's value.

# Condition
## If
`If` statement with a short condition

```go
if v := math.Pow(x, n); v < lim {
		return v
}
```

Variables declared inside an `if` short statement are also available inside any of the `else` blocks.

# Switch
Switch cases evaluate cases from top to bottom, stopping when a case succeeds.  
In effect, the `break` statement that is needed at the end of each case in those languages is provided automatically in Go.  
Another important difference is that Go's switch cases need not be constants, and the values involved need not be integers.

## Switch with No Condition
Switch without a condition is the same as `switch true`.  
This construct can be a clean way to write long if-then-else chains.

