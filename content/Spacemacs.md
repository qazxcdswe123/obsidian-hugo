[From VIM](https://develop.spacemacs.org/doc/VIMUSERS.html)
## Mode and State
In vim you have various editing modes like `insert mode` and `visual mode` to manipulate text. In Emacs, we have [states](https://develop.spacemacs.org/doc/DOCUMENTATION.html#states). These are equivalent to vim modes. For example, `evil-insert-state` is the same as `insert-mode` in vim.
A `minor-mode` in Emacs is like a feature that is activated. For example, `aggressive-indent-mode` is a `minor-mode` that automatically indents code as you type. It is important to know that there can be many `minor-modes` activated in a buffer. Many Emacs packages work by providing a `minor-mode`. A `major-mode` determines the editing behavior of Emacs in the current buffer. There is generally a corresponding `major-mode` per filetype. An example of a `major-mode` is `python-mode`, which provides python specific settings in python files. There is only one `major-mode` per buffer.
Layers are similar to vim plugins. They provide new features to use in Spacemacs. However, layers are often comprised of several packages that integrate well with each other. For example, the `python` layer includes support for auto-completion, documentation look-up, tests, and much more by using several different packages.
## Key-binding
All key bindings are mnemonic and are organized under the `<Leader>` key. For example, the key bindings for language-specific commands are always under the `SPC m` prefix. A full list of conventions used in Spacemacs is [here](https://develop.spacemacs.org/doc/CONVENTIONS.html). Note that all key bindings can be changed.
## Buffer
Buffers in Emacs and vim are essentially the same. The key bindings for buffers are located under the `SPC b` prefix.
| Key binding                       | Function                                                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `SPC b b <buffer-name>`   | Create a buffer named `<buffer-name>`.                                                                                  |
| `SPC b b`                 | Search through open buffers and recent files.                                                                           |
| `SPC b n` or `:bnext`     | Switch to the next buffer. (See [Special buffers](https://develop.spacemacs.org/doc/VIMUSERS.html#special-buffers))     |
| `SPC b p` or `:bprevious` | Switch to the previous buffer. (See [Special buffers](https://develop.spacemacs.org/doc/VIMUSERS.html#special-buffers)) |
| `SPC b d` or `:bdelete`   | Kill current buffer.                                                                                                    |
| `SPC b C-d`               | Kill all buffers except the current buffer.                                                                             |
## Windows
Windows are like splits in vim. They are useful for editing multiple files at once. All window key bindings are under the `SPC w` prefix.
| Key binding            | Function                             |
| ---------------------- | ------------------------------------ |
| `SPC w v` or `:vsplit` | Opens a vertical split on the right. |
| `SPC w s` or `:split`  | Opens a horizontal split below.      |
| `SPC w h/j/k/l`        | Navigate among windows.              |
| `SPC w H/J/K/L`        | Move the current window.             |
## Files
| Key binding | Function                                                     |
| ----------- | ------------------------------------------------------------ |
| `SPC f f`   | Opens a buffer to search for files in the current directory. |
| `SPC f r`   | Opens a buffer to search through recently opened files.      |

To quit a partially entered command, type C-g.
## Set Mirror
[Src](https://uyaki.github.io/post/spacemacs%E6%B8%85%E5%8D%8E%E6%BA%90%E9%95%9C%E5%83%8F%E5%8A%A0%E9%80%9F/)
