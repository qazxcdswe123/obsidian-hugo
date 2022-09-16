---
aliases: []
tags: []
date created: Sep 9th, 2022
date modified: Sep 9th, 2022
---

## Keymap
- Use [[Vim]]  
- Config: Keymap -> Editor -> Up/Down set to `CMD+K/J` (Keep old)
- `System Preferences | Keyboard | Shortcuts | Services` and disable `Search man Page Index in Terminal` to use 
	- `CMD+Shift+A` to find actions

### Easymotion
```
set easymotion
map f <Nop>
map F <Nop>
nmap f <Plug>(easymotion-f)
nmap F <Plug>(easymotion-F)
```

### NERDTree
[NERDTree support · JetBrains/ideavim Wiki · GitHub](https://github.com/JetBrains/ideavim/wiki/NERDTree-support)

[[Google Test]]