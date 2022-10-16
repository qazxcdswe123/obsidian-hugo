---
aliases: []
tags: []
date created: Sep 14th, 2022
date modified: Sep 16th, 2022
---
[[Test Mocking]]  
[Software testing - Wikipedia](https://en.wikipedia.org/wiki/Software_testing)

## General
Good practices for unit testing include:
- Creating tests for all publicly exposed functions, including class constructors and operators.
- Covering all code paths and checking both trivial and edge cases, including those with incorrect input data (see [negative testing](https://en.wikipedia.org/wiki/Negative_testing)).
- Assuring that each test works independently and doesn't prevent other tests from execution.
- Organizing tests in a way that the order in which you run them doesn't affect the results.

## Language
- [[C++ Testing]]
	- [JetBrains Docs](https://www.jetbrains.com/help/clion/unit-testing-tutorial.html#basics)  
- [[JavaScript JEST]]
- [[Python Testing]]
- [[Go Testing]]


## Soak Test
[Soak testing - Wikipedia](https://en.wikipedia.org/wiki/Soak_testing)
Running for a long time under average load.
This falls under [load testing](https://en.wikipedia.org/wiki/Load_testing "Load testing").

## Practices
[[BDD]]
[[TDD]]