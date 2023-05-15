---
aliases: []
date created: Apr 30th, 2023
date modified: Apr 30th, 2023
---
在看到 [Lazycat 的 Twitter](https://twitter.com/manateelazycat/status/1649962719502798848) 评价编程语言之后，也有了评价 (roast) 编程语言的念头。正好 22 级有挺多编程语言相关问题，随手吐槽一下  
Disclaimer: 本人只是练习编程时长一年半的大二学生，hot takes only。同时也不是每个语言都深入写过，就当每个语言只写过 hello world 的程度吧。 全是个人偏见，欢迎各位大佬补充。  
想到啥写啥
- [Lazycat 全文链接](https://threadreaderapp.com/thread/1649962719502798848.html)

1. [[Learn C in 1 Hour|C]]  
接触的第一门语言，作为入门语言教会了我指针，函数，变量，循环这些基础内容，印象最深的是：一开始写的代码过几个月看好丑：D  
到了现在，感觉 C 本身其实是非常简单的语言，甚至可以说是最简单的那一批，它的 simplicity 我觉得真的是无可替代的。  
除此之外，学 C 也是学 x86 assembly 的非常好的一个垫脚石，而且现有的 C Codebase 也非常重要 ([[Linux Kernel|kernel]], libc etc.) 可以说是 “计算机科学” 必备的一门语言，可以说不是程序员选择写 C，而是 C 选择了程序员。  
hot take: simple and unsafe  
学习途径：ThinkC + CS50

2. [[C++]]  
学校教学语言，谭浩强的书：）。接触的第二门语言  
C++ 也是工业中不可或缺的一部份了，也是无可取代。挺多特点挺牛的，无缝 `extern "C"` ，move semantics, std library，`string_view` etc.  
但是坦白说，不喜欢，非常非常的复杂，只有 C 的语法，但是和 C 完全是两个相反的东西，一个非常简单一个非常复杂，特别是 Modern C++ (主要是 17, 20) 的一些 `std::` 真的挺雷人。  
但是写 Modern C++ (主要是 11 14) 又挺有意思的，写起来体验偶尔还行。  
hot take: complex and unsafe (by design!!!)  
学习途径：网络自学 + 吃 C 老本

3. [[Rust]]  
[Learn Rust in 3 Minutes](https://www.youtube.com/watch?v=cE0wfjsybIQ)  
为了 memory safety 牺牲了很多随性，但是写起来手感意外的不错，但是复杂复杂复杂好复杂。  
非常喜欢它的 error handling 和 fearless concurrency，和一些 api 的设计。  
Compiler 做的真不错，很多时候看 error message 就能改出来，但是写起来心智负担挺重的，心理地位中上  
除此之外占用储存挺多的，也是槽点，dependencies 和 cache 和 binary 都好大。。  
好多 rust tools， 比如说 fd 和 rg 真好用！！  
hot take: safe by design, complex and safe  
学习途径：Rusting + Rust Book + Rust By Example

4. [[Python]]  
我听说的第一门语言，写起来手感非常顺，但是感觉坑会比较多，特别是年少不知 pip dependencies 和 system dependencies 撞之后的后果，花了很多时间解决这些琐事。  
科学计算和数据处理已经离不开了，相关领域必备技能  
整体非常简单  
个人感觉难点是 generator，asyncio，scheduler，GIL 还有各种 library 这方面  
主要槽点是性能不太行，还有 `try` 之后不是 `catch` 是 `except` ：（  
学习途径：Python 官方 Tutorial

5. [[Java]]  
OOP by design，工业届宠儿，说实话用来写工业代码真的很不错。  
槽点是写起来没啥激情，感觉就像在拧螺丝一样，毕竟每个人都是希望自己特殊一点的。  
但是如果我要选技术可能我也是选 java  
很喜欢它的 explicit exception in function signature  
还有一个槽点是万年 jdk8  
学习途径：吃老本 + Oracle Tutorial + 写项目（CS186 DB Project）

6. Scheme/Lisp/Elisp  
学 [[SICP]] 时候的语言，括号看的难受，但是真写起来这些 functional 的东西真的挺带感的，写起来骂娘，但不写一段时间又会想起来。。。  
没学很深，但是真挺带感的  
学习途径：折腾 Emacs （已转 [[Vim|Neovim]]）+ SICP

7. Ocaml  
写过一些，没有过多接触，槽点主要是 explicit `rec`，但没写很深，总体感觉挺有意思的  
还有编译之后是 shebang `#!/usr/bin/env ocamlscript` + compiled bytecode 作为纯文本存，真的难顶，笑死我了。  
学习途径：官方教程

8. [[Lua]]  
为了 [[Vim|Neovim]] 学的语言，整体非常简单，可能是最简单的语言，但是坑也挺多，主要是 type 和 index starts at 1  
感觉大型项目写不起来，整体比较散  
同样，没学很深（但是感觉基本学完了，内容真的很少）  
学习途径：官方文档 + Learn X in Y minitues + nvim

9. [[Golang]]  
手感和 [[Python]] 类似，simple by design！写起来很顺。  
第一印象不行（在第一次学 Go Tour 的时候，感觉好丑，选择看起来感觉还行吧）  
error handling 有点丑，但是我觉得是好事，explict error handling is a virtue  
整个工具链非常成熟，一个 `go` 把所有管完  
挺喜欢 `channel` 和 `waitGroup` 的设计的
还是感觉挺丑的。。。  
学习途径：Go Tour + 官方 doc + Go by example + The Go PL

10. [[JavaScript]]  
写起来很爽，真的很爽，错起来非常容易，null + undefined + NaN，直接变身 NaNi / BaNaNa  
可以说是这个世界不可替代的一部份了，NodeJS + npm = All in one  
闭括号要闭一堆括号真的晃眼  
整体来说不喜欢  
感觉已经和英语一样变成程序员的“世界语”了，不会就无法交流  
还有一个槽点是它（前端）的 build tools 太多了好复杂 (webpack, parcel, rollup, vite, turbo, esbuild just to name a few)，还有一万个 config file 真的难顶  
还有就是 node 好重，感觉 deno 挺小清新的但是没有非常方便的支持 npm 就是不爽 (yes i know it supports npm now but not as native as node)  
学习途径：modern js tutorial + 各种乱七八糟想逃都逃不掉的地方，到处都有 js 真无语。。

11. [[TypeScript]]  
既然 JS 横行已经是定局，打不过就加入，加入就加 TS 准没错，explicit typing 我最喜欢了，终于没 baNaNa 了 (anyscript warning)  
除了不喜欢 Nodejs 和前端那一套和又多加了一个 `tsconfig` 之外，我非常喜欢这门语言，几乎没有槽点  
学习途径：官方 handbook + 逃不过就加入的各种 JS/TS 项目

12. [[Frontend]]: [[CSS]] + HTML + JSX/TSX  
感觉把整个前端拉出来聊聊没问题

- CSS 我是又爱又恨，恨是因为 CSS 真不好写，感觉很吃经验和积累，爱是因为好用也真好用，而且 Tailwind CSS 真不错。
- HTML，正经人谁还写 HTML，不都 JSX 一把梭了。
- JSX，想出这玩意的真是个人才，加上 [[ReactJS]]/[[Vuejs]] 手感意外非常不错  

前端的槽点，基本就是 js 的槽点吧  
希望这辈子能给 V8/NodeJS 贡献些代码减少碳排放（晕）  
学习途径：野路子 + 读写项目

13. Haskell + Perl  
这两个只接触过一些，没写过，但是好丑好丑好丑好丑

14. [[Shell]] Script  
用来解决燃眉之急很不错，一次性语言，到处拉屎（晕）  
坑非常非常非常多，语法非常诡异，每次都是查语法，写起来云里雾里。  
如果加上 ShellCheck 限制就非常多，不加写起来非常容易出错  
学习途径：天下 Shell Script 一大抄（笑

15. [[CMake]] + [[Makefile]]  
严格来说是 Domain Specific Language 吧，不算编程语言，放进来凑个 15  
写起来好难受，可能是写起来不太习惯，但是写好了放那不管也挺方便的。  
学习途径：CMake 是官方教程，Makefile 是上网冲浪