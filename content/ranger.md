Parents:: [[Vim]]

`zh` = show hidden
空格选中一个文件，对选中的文件再按空格取消选中
`ranger --copy-config=all` copy config to 
install `highlight` to preview code

## Bookmark
`m` + key to save a bookmark
use `'` to navigate

## Basic keybinding
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

## config
### rc.conf
```
# Use yc to copy content to system clipboard 
map yc shell cat %p | xclip -sel clip
```
