- `-r`  recursive
- `-a` This option not only syncs recursively, but also preserves attributes such as symbolic links, file ownerships, permissions [[Linux User]], and modification times.
- `-v` prints out the syncing process in verbose.
- `--delete` delete files in destination folder when it was deleted in source folder
- `-P` see Progress
- `-h` human readble

- Example
`rsync -Pravh --delete Notes/ ~/code/hugo/content`
