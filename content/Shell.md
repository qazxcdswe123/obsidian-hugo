---
aliases: [zsh]
date created: Jul 8th, 2022
date modified: Apr 1st, 2023
---

## Movement
- `ALT+F` to jump **F**orward by a word.
- `ALT+B` to jump **B**ackward by a word.
- `CTRL+F` to move forward by a char
- `CTRL+B` to move backward by a char
- `CTRL+A` to jump to start of the line
- `CTRL+E` to jump to end of the line
- `CTRL+K` to kill the line starting from the cursor position
- `ALT+D` to delete a word starting from the current cursor position
- `CTRL+W` to remove the word backwards from cursor position
- `CTRL+R` to reverse search for commands you typed in the past from your history.
- `CTRL+S` to forward search (works in ZSH for me but not bash)

## ZSH
- [Home | Zim: Modular, customizable, and blazing fast Zsh framework](https://zimfw.sh/)

## Scripting
- To assign a variable, use = **without** space
- To use a variable, simply add $ before it
- `set -x` Show what's executed
- `set -e` If the return code of one command is not 0 and the caller does not check it, the shell script will exit. This feature make shell script robust.

- `$0` - Name of the script
- `$1` to `$9` - Arguments to the script. `$1` is the first argument and so on.
- `$@` - All the arguments
- `$#` - Number of arguments
- `$?` - Return code of the previous command
- `$$` - [[Process]] identification number (PID) for the current script
- `!!` - Entire last command, including arguments. A common pattern is to execute a command only for it to fail due to missing permissions; you can quickly re-execute the command with sudo by doing `sudo !!`
- `$_` - Last argument from the last command. If you are in an interactive shell, you can also quickly get this value by typing `Esc` followed by `.` or `Alt+.`

## Links
- [missing.csail.mit.edu](https://missing.csail.mit.edu/2020/shell-tools/)  
- [[Modern Linux Command]]
- [[SSH]]
- [[IO]]
- [[iTerm2]]
