- Used in Neovim
- [Learn Lua in Y Minutes](https://learnxinyminutes.com/docs/lua/)

## General
- All numbers are double
- No `++` / `+=`
- string is immutable by default
- `~=`: not equal, ok for string
- var global by default (Use `local`)
- String concatenation uses the `..` operator:
- **Only nil and false are falsy; 0 and '' are true!**

### Condition
```lua
-- Blocks are denoted with keywords like do/end:
-- While clause:
while num < 50 do
  num = num + 1  -- No ++ or += type operators.
end


-- If clauses:
if num > 40 then
  print('over 40')
elseif s ~= 'walternate' then  -- ~= is not equals.
  -- Equality check is == like Python; ok for strs.
  io.write('not over 40\n')  -- Defaults to stdout.
else
  -- Variables are global by default.
  thisIsGlobal = 5  -- Camel case is common.

  -- How to make a variable local:
  local line = io.read()  -- Reads next stdin line.

  -- String concatenation uses the .. operator:
  print('Winter is coming, ' .. line)
end


-- 'or' and 'and' are short-circuited.
-- This is similar to the a?b:c operator in C/js:
ans = aBoolValue and 'yes' or 'no'  --> 'no'


-- Use "100, 1, -1" as the range to count down:
-- Include both end
-- Start from 1
fredSum = 0
for j = 100, 1, -1 do fredSum = fredSum + j end
```

### Function
```lua
-- Closures and anonymous functions are ok:
function adder(x)
  -- The returned function is created when adder is
  -- called, and remembers the value of x:
  return function (y) return x + y end
end
a1 = adder(9)
a2 = adder(36)
print(a1(16))  --> 25
print(a2(64))  --> 100


function bar(a, b, c)
  print(a, b, c)
  return 4, 8, 15, 16, 23, 42
end

x, y = bar('zaphod')  --> prints "zaphod  nil nil"
-- Now x = 4, y = 8, values 15...42 are discarded.
```

### Tables
Similar to php arrays or js objects, they are hash-lookup dicts that can also be used as lists.
```lua
-- Dict literals have string keys by default:
t = {key1 = 'value1', key2 = false}


-- String keys can use js-like dot notation:
print(t.key1)  -- Prints 'value1'.
t.newKey = {}  -- Adds a new key/value pair.
t.key2 = nil   -- Removes key2 from the table.


for key, val in pairs(u) do  -- Table iteration.
  print(key, val)
end


-- _G is a special table of all globals.
print(_G['_G'] == _G)  -- Prints 'true'.


-- List literals implicitly set up int keys:
v = {'value1', 'value2', 1.21, 'gigawatts'}
for i = 1, #v do  -- #v is the size of v for lists.
  print(v[i])  -- Indices start at 1 !! SO CRAZY!
end
```

### Module
```lua
-- Suppose the file mod.lua looks like this:
local M = {}

local function sayMyName()
  print('Hrunkner')
end

function M.sayHello()
  print('Why hello there')
  sayMyName()
end

return M

-- Another file can use mod.lua's functionality:
local mod = require('mod')  -- Run the file mod.lua.

-- require is the standard way to include modules.
-- require acts like:     (if not cached; see below)
local mod = (function ()
  <contents of mod.lua>
end)()
-- It's like mod.lua is a function body, so that
-- locals inside mod.lua are invisible outside it.

-- This works because mod here = M in mod.lua:
mod.sayHello()  -- Says hello to Hrunkner.

-- This is wrong; sayMyName only exists in mod.lua:
mod.sayMyName()  -- error

-- require's return values are cached so a file is
-- run at most once, even when require'd many times.
```