---
aliases: []
date created: Jun 26th, 2022
date modified: Mar 12th, 2023
---
[[Python Numpy]]  
[Docs](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

# Series
- Parameters
	- **data**: array-like, Iterable, dict, or scalar value
		- Contains data stored in Series. If data is a dict, argument order is maintained.
	- **index**: array-like or Index (1d)
		- Values must be hashable and have the same length as data. Non-unique index values are allowed. Will default to RangeIndex (0, 1, 2, …, n) if not provided. If data is dict-like and index is None, then the keys in the data are used as the index. If the index is not None, the resulting Series is reindexed with the index values.

Numpy 中的一维数组没有索引，而 Series 对象具有索引。创建 Series 时可以不指定索引，系统添加自动索引，其值从 0 开始至元素个数减 1。

# DataFrame
[Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)  
Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.
- Parameters
	- 
