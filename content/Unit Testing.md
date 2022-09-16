---
aliases: []
tags: []
date created: Sep 14th, 2022
date modified: Sep 16th, 2022
---
[[Mocking]]  
[JetBrains Docs](https://www.jetbrains.com/help/clion/unit-testing-tutorial.html#basics)  

## General
Good practices for unit testing include:
- Creating tests for all publicly exposed functions, including class constructors and operators.
- Covering all code paths and checking both trivial and edge cases, including those with incorrect input data (see [negative testing](https://en.wikipedia.org/wiki/Negative_testing)).
- Assuring that each test works independently and doesn't prevent other tests from execution.
- Organizing tests in a way that the order in which you run them doesn't affect the results.

## Language
- C++
	- [[C++ Catch2]]

## Pattern
### BDD
[Behavior-driven development - Wikipedia](https://en.wikipedia.org/wiki/Behavior-driven_development)  

BDD focuses on:
- Where to start in the process
- What to test and what not to test
- How much to test in one go
- What to call the tests 
- How to understand why a test fails  
[Test-driven development - Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development)