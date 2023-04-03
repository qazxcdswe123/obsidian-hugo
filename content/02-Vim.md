---
aliases: []
date created: Mar 5th, 2022
date modified: Jul 25th, 2022
---
# 前言
  其实不久之前，我对 Vim 的评价还是花里胡哨的，有这时间学 Vim 不如学点其他的，VSCode 不香吗，就搁着装逼呢？
  VSCode 香死了，几乎零配置成本，开箱即用，插件多多，然而用了一段时间 Vim 后，我已经被它这种文本编辑模式和高度的可自定义性所吸引，回不去了 :(
  可能下面很多东西都花里胡哨的，不过就我来说，我用得很爽 :D ，不服不辨。
  本文不讲使用，只介绍。
  ___
  另外推荐使用版本较新的 [Neovim](https://neovim.io/)，相对于原版 Vim 功能更丰富，插件更多。最好不要用 Debian Ubuntu 自带的老版本，部分插件不支持。

# 原生 Vim
## Vim学习
网上有很多了，重要的是跟着做，十分推荐用 Neovim 的 Vimtutor，左侧是带批改的。
## Vim 的局限
1. 上手难，估计用上几年都能发现新东西
2. 十分十分耗时间，自定义选项特别多（当然也是优势，搞 Vim 就要有养成的觉悟）
## Vim 额外功能
1. `:term full-program-name` 直接在 Vim 里面运行终端程序
2. `<C+v>` 矩形选择，对于添加注释有用
# 自定义 Vim
## 配置文件
如果使用 Vim, 文件为 `.vimrc` , 如果使用 Neovim, 文件为`$HOME/.config/nvim/init.vim` (要自己新建)
可在 Github 上搜 `dotfiles` 可参照别人的配置文件进行修改
## 为 Vim 安装插件
修改 Vim 配置文件，为 Vim 添加各类插件
目前主流的有两个 Vim 插件管理器，一个是[Vim-Plug](https://github.com/junegunn/vim-plug) , 另一个是 [dein.vim](https://github.com/Shougo/dein.vim) ，作为两者的区别为 Vim-Plug 老牌，十分易用，而 dein 作为较新（历史不新技术新）的插件管理器会更快，但相对来说易用性差一点（其实在插件少的情况下，感觉没啥区别），更推荐使用 Vim-Plug
插件管理器的安装请参照上方给出的 Repo 说明，主要一点就是要能终端访问 Github ，插件基本都是从 Github 上面下的。
### 插件推荐
Vim 比 VSCode 相差最大的我觉得就是 Vim 没有一个统一的扩展商店，Vim 插件不好找（而且也不知道有这个需求），很多时候是靠 dotfiles 间相传，这里推荐一些很基础的，人人都需要的。
- [解决输入法1](https://github.com/daipeihust/im-select) [解决输入法2](https://www.zhihu.com/question/303850876) [解决输入法3](https://sspai.com/post/71322) 最简单就是代码不打中文。
- [coc.nvim 自动补全+额外插件](https://github.com/neoclide/coc.nvim) coc 是插件，但你可以给插件安插件
- [括号补全](https://github.com/jiangmiao/auto-pairs)
- [括号增强1](https://github.com/tpope/vim-surround) + [括号增强2](https://github.com/gcmt/wildfire.vim) 混合使用有奇效 [教程](https://www.bilibili.com/video/BV1KT4y1c78p)
## 和 WSL 中的 Linux 共享剪贴板
[source](https://github.com/neovim/neovim/wiki/FAQ#how-to-use-the-windows-clipboard-from-wsl) 
```
curl -sLo/tmp/win32yank.zip https://github.com/equalsraf/win32yank/releases/download/v0.0.4/win32yank-x64.zip
unzip -p /tmp/win32yank.zip win32yank.exe > /tmp/win32yank.exe
chmod +x /tmp/win32yank.exe
sudo mv /tmp/win32yank.exe /usr/local/bin/
```
完全共享剪贴板只要在 `init.vim` 或 `.vimrc` 中添加一行 `set clipboard=unnamedplus` ，来修改 Vim 的剪贴板位置（不推荐，使得原生寄存器功能缺失，但确实很方便）
## Vim 的剪贴板
更准确来说是 Vim 的寄存器(Register)，了解一下不难，但不了解的话复制粘贴都是问题。
https://www.brianstorti.com/vim-registers/
# 额外折腾
	- [difference between the remap, noremap, nnoremap and vnoremap mapping commands in Vim](https://stackoverflow.com/questions/3776117/what-is-the-difference-between-the-remap-noremap-nnoremap-and-vnoremap-mapping) （对自定义很有用）
	- [我的折腾领路人](https://space.bilibili.com/13081489/video)
	- [Text Object](https://blog.carbonfive.com/vim-text-objects-the-definitive-guide/)
# Vim 以外
Vim 的理念私以为减少离开键盘，避免在鼠标键盘间的来回切换，那在代码以外的领域也是这样的，很多情况下对一些常用的功能（打开文件夹，打开软件）也是可以用快捷键进行操作。一些系统自带的快捷键很好用，想自定义快捷键的话这里推荐软件 [AutoHotkey](https://www.autohotkey.com/) 来自定义快捷键。
有个非常极端的使用例子来自 LinuxTechTips 的首席剪辑师 Taran，日常剪片时候用五个键盘，四个键盘专门用于快捷键的存放，主要使用的就是 [AutoHotkey](https://www.autohotkey.com/) 
![](https://s2.loli.net/2022/01/31/t7IUVGgRTdQxCu8.jpg)
具体使用方法请 Google `Taran macro king` （国内字幕翻译为宏孩儿 xD）或看他存放配置文件的 [Repo](https://github.com/TaranVH/2nd-keyboard) 他也在 LTT 和自己的频道出过几个视频演示，还蛮有意思的。
还有 Chrome 下的 Vim 扩展 [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb) `d` 键滚屏和 `JK` 切 Tab 太香了。
## TUI
除了熟知的 `GUI` ，其实还有 `TUI`(Terminal UI)，在终端中的界面，用的好的话，完全可以像 `Emacs` 一样成为操作系统，稍微介绍一些软件。
- 终端下的文件管理器 [ranger](https://github.com/ranger/ranger) 切文件前所未有的快
- 终端下的 Git UI [lazygit](https://github.com/jesseduffield/lazygit)，简化 Git 操作，Windows terminal 需要在 Profile 下的 Appearance 中开启 Text Formatting 下的 Bold font with bright colors
- tmux 必备，或类似多终端软件
- 配置好的 zsh
# 随想
- 什么时候觉得 `ESC` 太远了，什么时候就算熟悉 Vim 了，Normal Mode 是最常待的 Mode，`u` 的 undo 应该最小化
- 真的很浪费时间啊，不过用起来确实很爽啊
- 我学的很浅，我也还在学-.-
  
<!--stackedit_data:
eyJwcm9wZXJ0aWVzIjoidGFnczogJ0NMSSxMaW51eCdcbiIsIm
hpc3RvcnkiOlstMTQ2NzI3OTAwMV19
-->
