---
aliases: [正则表达式, regular expression]
tags: [] 
date created: Mar 28th, 2022
date modified: Feb 14th, 2023
---
[[Finite State Machine]]

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

## Regex in [[SQL]]
- [[SQL Query]]

### Old School
- `WHERE S.sname LIKE 'B_%'`

### Standard Regex
- `WHERE S.sname ~ '^B.*'`