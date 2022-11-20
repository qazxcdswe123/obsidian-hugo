---
aliases: []
tags: []
date created: Nov 18th, 2022
date modified: Nov 18th, 2022
---

## What
Use dictionary to compress a ASCII encoded text.  
Work best with repeated words.

## How
Input: text: A sequence of characters in the ASCII character set.  
Output: A sequence of indices into a dictionary.
1. For each character c in the ASCII character set: 
	1. A. Insert c into the dictionary at the index equal to c’s numeric code in ASCII.
2. Set s to the first character from text.
3. While text is not exhausted, do the following: 
	1. A. Take the next character from text, and assign it to c.  
	2. B. If s c is in the dictionary, then set s to s c.  
	3. C. Otherwise (s c is not yet in the dictionary), do the following: 
		1. i. Output the index of s in the dictionary.  
		2. ii. Insert s c into the next available entry in the dictionary.  
		3. iii. Set s to the single-character string c.
4. Output the index of s in the dictionary.

## Why