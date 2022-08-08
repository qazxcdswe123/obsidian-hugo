---
aliases: [正则表达式]
tags: []
date created: Mar 28th, 2022
date modified: Jul 31st, 2022
---
- nfa dfa [[todo]]
- [nfa and dfa](https://www.geeksforgeeks.org/difference-between-dfa-and-nfa/)

| Character | Explain                                                                  |
| --------- | ------------------------------------------------------------------------ |
| `.`       | any char                                                                 |
| `*`       | 0 or more times                                                          |
| `+`       | 1 or more times                                                          |
| `?`       | optional char                                                            |
| `{m, n}`  | repeat m to n times                                                      |
| `\d`      | Any Digit                                                                |
| `\w`      | matches any single letter, number or underscore (same as `[a-zA-Z0-9_]`) |
| `\s`      | white space                                                              |
| `()`      | _back-references_ (or _capturing groups_), stored in variable                                                                         |