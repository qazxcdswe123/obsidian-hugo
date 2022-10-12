---
aliases: [Neovim, nvim]
tags: [] 
date created: Jul 11th, 2022
date modified: Oct 8th, 2022
---
- [[02-Vim]]
- [[ranger]]
# Vim
## Text
- `daw` delete word under cursor
- `d/cib` - delete a block surrounded by (
- `d/ciB` - delete a block surrounded by {
- `d/cas` - delete a sentence
- `d/cap` - delete a paragraph

## Windows
`CTRL-W=` equal size  
`CTRL-W-` decreases the current window  
`:vsp` vertically split windows  
`:e` edit new file in current buffer  
`<C-^>` quickly switch buffer (this and before, only 2 buffers will be loaded)

## Dot `.`
Can be used only after text is changed

## Macros
[Macros | Vim Tips Wiki | Fandom](https://vim.fandom.com/wiki/Macros)
`q<letter><commands>q` where letter is `a-z`  
`<number>@<letter>` to use

## Movements
`JK` move 5 lines  
`R` replace more char
`HL` move to beginning or end, equivalent to `^$` 
	
## Indent
`<G` / `>G` to indent (`.` to repeat)

## Tricks
- Write as sudo
	- `:w !sudo tee%`
- Set `-` as a word
	- `set iskeyword+=-`

## Plugins
### Nvim-surround
[GitHub - kylechui/nvim-surround: Add/change/delete surrounding delimiter pairs with ease. Written with in Lua.](https://github.com/kylechui/nvim-surround)
- ys
- cs
- ds

- **function manipulation**:
	- `ysiwffunc`
	- `dsf`
	- `csfnew_name`
