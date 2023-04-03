---
aliases: []
tags: [] 
date created: Jul 13th, 2022
date modified: Mar 22nd, 2023
---
- [[Git Command]]
- [Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
	- `git config --global credential.helper store`

## Reset
[version control - What's the difference between git reset --mixed, --soft, and --hard? - Stack Overflow](https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard)

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
	

### Squash
[git - How do I squash my last N commits together? - Stack Overflow](https://stackoverflow.com/questions/5189560/how-do-i-squash-my-last-n-commits-together)

### Pretty Print
`git ls-tree --full-tree --name-only -r HEAD`  
`git log --all --decorate --oneline --graph`

### Sparse Checkout
```
git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/cirosantilli/test-git-partial-clone
  
cd test-git-partial-clone
git sparse-checkout set path/to/dir
```

## Argument
- `-C` run in specific directory `git -C ~/.SpaceVim pull`
- `-filter` 
	- The form **--filter=blob:none** omits all blobs.

## Git Object
Now, **what actually is a Git object?** At its core, Git is a “content-addressed filesystem”. That means that unlike regular filesystems, where the name of a file is arbitrary and unrelated to that file’s contents, the names of files as stored by Git are mathematically derived from their contents. This has a very important implication: if a single byte of, say, a text file, changes, its internal name will change, too. To put it simply: you don’t _modify_ a file, you create a new file in a different location. Objects are just that: files in the git repository, whose path is determined by their contents.
- [[git submodule]]
___
[[Lazygit]]