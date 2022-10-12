---
aliases: []
tags: [] 
date created: Sep 27th, 2022
date modified: Sep 28th, 2022
---
[[Go Struct]]

## Zero Values
Variables declared without an explicit initial value are given their _zero value_.  
The zero value is:
- `0` for numeric types,
- `false` for the boolean type, and
- `""` (the empty string) for strings.
- `nil` for slice

```go
s := "" 
var s string 
var s = "" 
var s string = ""
```


## All Types

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```