---
aliases: []
tags: []
date created: Sep 27th, 2022
date modified: Oct 13th, 2022
---
# Math
## Math/rand
- `rand.Intn($UpperBoundNotIncluded)`

## Misc
In Go, a name is exported if it begins with a capital letter. For example, `Pizza` is an exported name, as is `Pi`, which is exported from the `math` package.

# Fmt
[fmt package - fmt - Go Packages](https://pkg.go.dev/fmt)

# OS
- `os.Open`
	- The function os.Open returns two values.
	- The firs t is an open file `(*os.File)` that is used in subsequent reads by the Scanner.
	- The second result of os.Open is a value of the built-in error type. If err equals the special built-in value nil, the file was opened successfully. The file is read, and when the end of the input is reached, `Close` closes the file and releases any resources.