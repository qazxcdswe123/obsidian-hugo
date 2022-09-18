---
aliases: []
tags: []
date created: Sep 18th, 2022
date modified: Sep 18th, 2022
---
# Unittest
[unittest — Unit testing framework — Python 3.10.7 documentation](https://docs.python.org/3/library/unittest.html)  

To achieve this, [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") supports some important concepts in an object-oriented way:
- test fixture
- A _test fixture_ represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

- test case
- A _test case_ is the individual unit of testing. It checks for a specific response to a particular set of inputs. [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") provides a base class, [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"), which may be used to create new test cases.

- test suite
- A _test suite_ is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

- test runner
- A _test runner_ is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.