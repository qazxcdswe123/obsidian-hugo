---
aliases: []
tags: []
date created: Jul 13th, 2022
date modified: Jul 25th, 2022
---
# Git
## Commit
附加修改提交信息
`git commit --amend "foobar"`

## Hacks
### Clear Git History
1. Checkout
    `git checkout --orphan latest_branch`
2. Add all the files
    `git add -A`
3. Commit the changes
    `git commit -am "commit message"`
4. Delete the branch
    `git branch -D main`
5. Rename the current branch to main
    `git branch -m main`
6. Finally, force update your repository
    `git push -f origin main`
	
### Pretty print
`git ls-tree --full-tree --name-only -r HEAD`
`git log --all --decorate --oneline --graph`

## Options
- `-C` run in specific directory `git -C ~/.SpaceVim pull`
- `-filter` 
- Save credential
	- `git config --global credential.helper store`
	- `git config credential.helper store`


- [[git submodule]]


___


[[Lazygit]]