---
aliases: []
date created: Jul 10th, 2022
date modified: Dec 9th, 2022
---
空格选中一个文件，对选中的文件再按空格取消选中  
`ranger --copy-config=all` copy config to `~/.config/ranger`  
install `bat` to preview code, configure `scope.sh` to set syntax highlight

## Plugins

### Zoxide
- Install:  
`git clone https://github.com/jchook/ranger-zoxide ~/.config/ranger/plugins/zoxide`
- Usage:  
`:z path` to jump  
`:zi` for interactive shell (config in zoxide)

## Bookmark
`m` + key to save a bookmark  
use `'` to navigate

## Basic Keybinding
`zh` = show hidden  
`g` for navigation and tabs  
`r` for :open_with command  
`y` for yank(copy)  
`d` for cut/delete  
`p` for paste  
`o` for sort  
`.` for filter_stack  
`z` for changing settings  
`u` for "undo"  
`M` for line mode  
`+`, `-`, `=` for setting access rights to files  
`F7`: mkdir

## Config

### rc.conf
```
# Use yc to copy content to system clipboard 
map yc shell cat %p | xclip -sel clip
```
