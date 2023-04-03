---
aliases: []
date created: Jan 28th, 2022
date modified: Jan 7th, 2023
---

# 前言
很早之前就知道有 Missing Semester 这门课程，但一直没花时间学，认为自己折腾的内容其实和所教授的内容差不多，以为自己已经学过了。  
但真正学了之后，才知道课程所涉及的广度和深度是自己捣鼓时很难学习到的，讲的很好很细，有基础的也可以看 [文字版](https://missing.csail.mit.edu) 学一下。  
本系列主要是自己的看法。**内容上尽量避免和原课程内容重复，只作为课程内容的补充**。~~原课程讲的很好了，也不知道补充啥好~~

## 对课程的一些评价
其实我还没学完，不过也快了，也许有些对该课程的发言权。  
若是看视频，隔着屏幕你都能感觉到三位讲师的热情，这是真的热爱，十分佩服。  
若是看文字档，真的能感到记录的很详细，讲的也很通俗，能把整个复杂的体系梳理成线性的，基本能 Self-contain 的教程，真的很了不起；对外部链接的扩展也很到位，若是想了解更多也不会没有方向；Exercise 的设置也还可以，网上也有 [答案](https://github.com/piaoliangkb/missing-semester-2020)。
___
缺点也是有的，首先是视频（也就是课堂上）基本就是不停的演示一连串的命令，可能相对枯燥，而且明显看得出时间卡的很紧，讲的很紧（但也没到快的程度，而且教这些内容确实无法避免枯燥的形式，课程 Note 的补充也弥补了这方面不足）。  
其次是其中一位讲师口音有点重，但他出现的视频下都有校对良好的人工字幕，问题也不大。  
总的来说，是很好的一门课。

# 正题
本文包含了以下章节内容
- [Course overview + the shell](https://missing.csail.mit.edu/2020/course-shell/) 无笔记，十分基础，作为课程入门，吃饭时候看挺下饭的
- [Shell Tools and Scripting](https://missing.csail.mit.edu/2020/shell-tools/) 主要讲了 
	- Shell Script 编程
	- $hebang (shebang) 的使用
	- 小技巧：通过 Shell 执行命令前，可以先用 `echo` 打出来检验命令正确性
- [Command-line Environment](https://missing.csail.mit.edu/2020/command-line/) 大体讲了
	- SIGNAL -- 为什么 Ctrl+c 能够停止程序，为什么有时候不能，Ctrl+z 又是什么，学会了可以结合 Lecture 2 的 Shell 写个脚本，考验你周边只会 Ctrl+c 的朋友 （然后周围没人用 Linux ）
	- 前台运行，后台运行 (bg, fg, nohup, &, jobs)
	- Tmux 神器，绝对值的好好学
	- SSH (Port forwarding, ssh-key, ssh_config)
	- ln 命令，软连接硬链接

## 命令行 (CLI)
在讨论会上提到，Shell 和 命令行是不一样的，GUI 也能是 Shell，只要起到了 Shell 的作用就是 Shell （Shell 九宫格）
___
想谈命令行（ Command Line Interface ），大概离不了 Linux，甚至，我认为 Linux 的灵魂，就在于 CLI，可以说学 Linux 就是在学 CLI。没有了 CLI 的 Linux 和 Windows 的区别就是，Windows 更好用。  
CLI 好在哪里，我们为什么要学它
- 从历史开始的，对各种编程语言原生适配
- 也是从历史开始的，编程相关工具的原生支持（git, vim)
- 对数据的 **高效** 处理 (pipe, grep, sed, awk, head, less, regex)
- 对参数的隐藏，使得其十分清爽，用熟了效率非常高，用过 Office 全家桶的都知道上面一栏功能全部列出来其实没那么方便。(GUI vs CLI)
- 对各类自动化，流水线的支持，发挥你的想象力，用 CLI 几乎无所不能 [例子](https://github.com/NARKOZ/hacker-scripts/blob/master/README.zh-CN.md)
- 服务器上基本都是 CLI，不用也得用
- 唯一的缺点就是门槛很高吧。。  
想要参与课程的学习，使用 LInux 下的 CLI 是必不可少的（Mac 请无视），十分推荐 Windows+WSL2+[Archwsl](https://fwing.notion.site/Archlinux-WSL2-setup-3ae01bed0b14418cbecc3a4605c97c3d) ，Ubuntu | Debian 也行 ，只要是 Linux CLI 均可，就本课程来说，不太需要虚拟机。**个人** 不太建议上 Linux 桌面，也不太推荐用大多数人推荐的 Ubuntu，而是推荐 Arch Linux。文末给出观点。
___

## Linux 文件权限
一直觉得很奇怪，为什么有 755 777 这样奇怪的数字？讨论会上提出来，才知道原来是掩码实现的。最大数字 7 即为 111
- **0 = ---**
- **1 = --x**
- **2 = -w-**
- **3 = -wx**
- **4 = r-**
- **5 = r-x**
- **6 = rw-**
- **7 = rwx**
___

## STDIO
Shell 由 IO 组成，与 C 语言的 `stdio.h` 和 C++ 的 `iostream` 共用一个 IO（大概），分别是 `STDIN` `0` && `STDOUT` `1` && `STDERR` `2`，Pipe 工作的原理也是如此，将上一个命令的 `STDOUT` 作为 `STDIN` 传入  
![](https://s2.loli.net/2022/01/22/lYD6QkncSuAbMZh.png)

## 软连接，硬链接
默认 ln 命令是硬链接，可以用 `-s` 实现软连接，这两者有什么区别？  
可以将软连接理解为快捷方式，硬链接理解为备份  
软连接实质上是指针，直接指向那个文件，删掉原始文件，将无法寻址
![](https://s2.loli.net/2022/01/22/Oup8fBFNxK9Pk4b.png)  
硬链接则是备份，只要硬盘上还有一份相连接，删掉任意一份也不会出事，而且占用空间极小，几个字节，不是一份源文件的 Copy  
![](https://s2.loli.net/2022/01/22/n8GOvrCJDFENZPf.png)

# 延申阅读

## Pipe
Pipe 的每个命令是并发的，你能想到吗：）  
[Pipe explained with STDIN and STDOUT](https://stackoverflow.com/questions/9834086/what-is-a-simple-explanation-for-how-pipes-work-in-bash)  
[How pipe works in detail](https://stackoverflow.com/questions/6893714/why-does-ps-o-p-list-the-grep-process-after-the-pipe)  
看完上面两篇，对 pipe 的原理，运作和使用一定会有更深的理解。  
Pipe 用的好，对数据处理那是真的方便  
经常与 pipe 联动的命令有
- grep
- cut
- sed
- awk
- less
- sort
- head
- tail

## Zsh
[OhMyZsh 管理器](https://github.com/ohmyzsh/ohmyzsh)  
推荐插件
- zsh-autosuggestions
- zsh-z
- colored-man-pages
- zsh-syntax-highlighting
- extract
- sudo  
[p10k theme](https://github.com/romkatv/powerlevel10k)  
[My dotfiles](https://github.com/qazxcdswe123/dotfiles) 注意，不要直接用别人的 dotfiles，要参考，要拿来，不要照抄，建议自己多加 alias 改善生活质量

## Tmux
[Missing Semester Lecture 5](https://missing.csail.mit.edu/2020/command-line/)  
[Tmux 教程](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)  
[Tmux 自定义配置](https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/)

## 光标移动
默认时基本和 Emacs 是类似的，但可以更改成为 vi 键位，不过命令行下的 vi 感觉用起来怪怪的
- Ctrl+ 左右键 : 在单词之间跳转
- Ctrl+a : 跳到本行的行首
- Ctrl+e : 跳到页尾
- Ctrl+u ：删除当前光标前面的文字 （还有剪切功能）
- ctrl+k ：删除当前光标后面的文字 (还有剪切功能)
- Ctrl+L：进行清屏操作
- Ctrl+y : 粘贴 Ctrl+u 或 ctrl+k 剪切的内容
- Ctrl+w : 删除光标前面的单词的字符（以空格隔开的字符串）
- Alt – d ：由光标位置开始，往右删除单词，往行尾删
- Ctrl+r : 搜索执行过的命令
- ! + 最近执行过的命令中的某个字符 ：可快速执行最近执行过的命令

## 命令学习
- [tldr](https://github.com/tldr-pages/tldr)
- [cheat](https://cheat.sh/)
- [经典命令的替代品](https://github.com/ibraheemdev/modern-unix)

## 不推荐 Linux 桌面的原因
首先，就课程来说不需要。齐次，Linux 桌面真的不好用，**日用软件** 生态，**驱动**，游戏等方面落后 Windows 一大截  
Linux 的特色就是自由，可自定义程度极高，演变出来各种发行版，可以说是玩出花来，但如果不是 Power User，私以为不会用得到这些自定义选项。  
Linux is free, only when your time is free  
为什么 Arch Linux 这么 [火](https://distrowatch.com/index.php?dataspan=score)，很大程度上是因为它的日用软件包最全最多，折腾反而少了。  
谈 Arch 色变的原因，主要是之前安装桌面环境真的蛋疼，而只用 CLI 的话，反而没这个问题，很轻松就能安装课程中提到的额外软件（tldr neovim etc.），版本还新，不容易出问题，桌面安装现在也很 [轻松了](https://wiki.archlinux.org/title/Archinstall_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))，官方脚本把先前劝退的步骤全部省略了，现在的 Arch 甚至反而适合新手用。  
Debian | Ubuntu 这类保守型发行版，很适合在服务器，老包稳定，不容易搞挂服务器，但日用选 Rolling，我觉得没问题。  
![](https://s2.loli.net/2022/01/22/X9gwoOzh4l1aTv3.png)

就 Linux 的精髓 CLI，Windows 已经抄过来了，不是开源 | 自由斗士，日用 Linux 桌面版并没有想象中那么好。  
不过我也认为，每个 Programmer 都应该尝试日用 Linux （属于是朝圣了）

![](https://s2.loli.net/2022/01/22/5lK92QngyWuheHs.jpg)

有错误请指出，欢迎补充
<!--stackedit_data:
eyJwcm9wZXJ0aWVzIjoidGFnczogJ0xpbnV4LCBDTEknXG4iLC
JoaXN0b3J5IjpbLTUzOTE3MjMzLDM1NjI0NDY1NywtMTgxOTYy
MjQ0N119
-->
