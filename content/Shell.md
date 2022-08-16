---
aliases: [zsh]
tags: [] 
---
[missing.csail.mit.edu](https://missing.csail.mit.edu/2020/shell-tools/)
[[Shell Tools and Scripting · the missing semester of your cs education]]
[[Linux Command Modern Alternative]]

# Shell
[[IO]]
- `2>&1`
File descriptor 1 is the standard output (`stdout`).  
File descriptor 2 is the standard error (`stderr`).

At first, `2>1` may look like a good way to redirect `stderr` to `stdout`. However, it will actually be interpreted as "redirect `stderr` to a file named `1`".
`&` indicates that what follows and precedes is a _file descriptor_, and not a filename. Thus, we use `2>&1`. Consider `>&` to be a redirect merger operator.

`&` is only interpreted to mean "file descriptor" in the context of redirections. Writing `command &2>&` is parsed as `command &` and `2>&1`, i.e. "run `command` in the background, then run the command `2` and redirect its stdout into its stdout".

# zsh
## Oh-My-Zsh
`sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"`

`git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`

`git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`

`git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

`git clone https://github.com/jeffreytse/zsh-vi-mode $ZSH_CUSTOM/plugins/zsh-vi-mode`

[[iTerm2]]