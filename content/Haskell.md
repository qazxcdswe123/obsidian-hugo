---
aliases: []
link: []
date created: Aug 1st, 2023
date modified: Nov 3rd, 2023
---

## List
- `++` and `:` for concatenation
- `head`, `tail`, `init`, `last`
- `reverse`
- `take num`, `drop num`
- `null`
- `elem`
	- `elem 'x' ['a', 'b', 'c']`
- `concat`
	- `concat [[3, 1], [2], [], [5, 10]]`
 - Linear time function
	- `length`
	- `!!` index
- range
	- `[1, 3 .. 20]`
		- `[1,3,5,7,9,11,13,15,17,19]`
	- `[10, 9 .. 1]`
		- `[10,9,8,7,6,5,4,3,2,1]`
	  - `[0 .. ]` infinite lists

## String
`list` of characters
- `word`
- `unword`

## Function

```haskell
functionName :: types
functionName arg1 ... argN = body


-- File   : Example.hs
-- Module : Example

module Example where

increase :: Integer -> Integer
increase x = x + 1
```

## Pakages
- **module** — a collection of functions and custom data types
- **package** — a collection of modules + metadata
- **Hackage** — a central repository of Haskell packages
- **base** — standard Haskell library
- **Prelude** — the module from **base** imported by default

- `import Data.List`

## Control Flow
- `if then else`
	- `price = if product == "milk" then 1 else 2`
- `guards`
- `case of`

```haskell
describe :: Integer -> String
describe n = case n of 0 -> "zero"
                       1 -> "one"
                       2 -> "an even prime"
                       n -> "the number " ++ show n
					   
-- parse country code into country name, returns Nothing if code not recognized
parseCountry :: String -> Maybe String
parseCountry "FI" = Just "Finland"
parseCountry "SE" = Just "Sweden"
parseCountry _ = Nothing

flyTo :: String -> String
flyTo countryCode = case parseCountry countryCode of Just country -> "You're flying to " ++ country
                                                     Nothing -> "You're not flying anywhere"
```

## Misc
- `let in`
- `where`

## `Maybe`

| Type       | Values                   |
|------------|--------------------------|
| Maybe Bool | **Nothing**, **Just False**, **Just True** |
| Maybe Int  | **Nothing**, **Just 0**, **Just 1**, ... |
| Maybe [Int] | **Nothing**, **Just []**, **Just [1,1337]**, ... |

```haskell
Prelude> :t Nothing
Nothing :: Maybe a
Prelude> Just "a camel"
Just "a camel"
Prelude> :t Just "a camel"
Just "a camel" :: Maybe [Char]   -- the same as Maybe String
Prelude> Just True
Just True
Prelude> :t Just True
Just True :: Maybe Bool
```

## `Either`

```haskell
-- right means correct
readInt :: String -> Either String Int
readInt "0" = Right 0
readInt "1" = Right 1
readInt s = Left ("Unsupported string: " ++ s)
```

## Constructor
Start with capital letter.

## Links
- [[List Comprehension]]
- [[Catamorphism]]