---
title: Vim
---
---
aliases: []
tags: [] 
---
[[02.Vim]]
[[ranger]]
# Vim
## Text
`daw` delete word under cursor
Count `<C-x>` reduce number
## Clipboard
`:%y+` copy all to clipboard
## Windows
`CTRL-W=` equal size
`CTRL-W-` decreases the current window
`:vsp` vertically split windows
`:e` edit new file in current buffer
`<C-^>` quickly switch buffer (this and before, only 2 buffers will be loaded)
## dot `.`
Available only after text is changed
## Macros
[Src](https://vim.fandom.com/wiki/Macros)
`q<letter><commands>q` where letter is `a-z`
`<number>@<letter>` to use
## Movements
`HJKL` move 5 lines
`setxkbmap -option caps:swapescape`  swap caps lock with esc key
`R` replace more char
`*` to highlight all occurrences and move between word under cursor
	Then use `n` to next occurrences
## Indent
`<G`, `>G` to indent (`.` to repeat)

## Tricks
- Write as sudo
	- `:w !sudo tee%`