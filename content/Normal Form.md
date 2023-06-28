---
aliases: []
date created: May 9th, 2023
date modified: Jun 27th, 2023
---
To solve the [[Database Anomaly]] problem.
> [[1NF]]：属性不可分割。
> 例如 关系模式：学生（姓名，住址），而住址又包含（区，街道），所以该模式不符合 1NF
> 
> [[2NF]]：不存在非主属性对候选码的部分依赖。
> 例如 已知候选码是 BC，非主属性是 D，函数依赖中除了 BC->D，还有 B->D 或者 C->D，该模式不符合 2NF
> 
> [[3NF]]：不存在非主属性对候选码的传递依赖。
> 例如 已知候选码是 AB，非主属性是 D，函数依赖中有 AB->C 和 C->D，所以该模式不符合 3NF
> 
> [[BCNF]]：不存在主属性对候选码的部分依赖和传递依赖。
> 
> 1.检查 R 中元素的 [闭包](https://so.csdn.net/so/search?q=%E9%97%AD%E5%8C%85&spm=1001.2101.3001.7020)，也就是哪些元素或者元素组合可以根据 F 中函数依赖关系得到完整的 R，这些元素或者元素组合就是候选码。这里 AB 的闭包是 ABC，记作 (AB)+=ABC，所以 AB 是候选码。
> 
> 2.通过候选码确定主属性和非主属性。这里 A，B 是主属性，剩下的 C 就是非主属性。
> 
> 3.判断范式标准：1NF，2NF，3NF，BCNF，4NF

- [[1NF]]
- [[2NF]]
- [[3NF]]
- [[BCNF]]
- [[4NF]]
- [范式判断的三个步骤以及各个范式标准(1NF,2NF,3NF,BCNF,4NF)\_怎么判断是否为bcnf范式\_土豆面包的博客-CSDN博客](https://blog.csdn.net/qq_40177015/article/details/111590534)
- [3NF分解与BCNF分解\_WKP9418的博客-CSDN博客](https://blog.csdn.net/qq_43179428/article/details/105596526)