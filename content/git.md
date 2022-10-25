---
aliases: []
tags: [] 
date created: Jul 13th, 2022
date modified: Oct 14th, 2022
---
[[GIt Hooks]]
# Git
## Config
[Telling Git about your signing key - GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)  
[Generating a new SSH key and adding it to the ssh-agent - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

```bash
git config --global gpg.format ssh
pbcopy < ~/.ssh/id_ed25519.pub
git config --global user.signingkey 'key'
git config --global commit.gpgsign true
git config --global tag.gpgsign true
git config --global color.ui auto
```

To get particular config value, use `--get`  
`git config --get --global color.ui`

To get all config value, use `--list`  
`git config --list`  
or look at your `~/.gitconfig` file. The local configuration will be in your repository's `.git/config` file.  
`git config --list --show-origin`

___
[Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- `git config --global credential.helper store`

## Commit
附加修改提交信息  
`git commit --amend "foobar"`

## Diff
- Compare with previous commit: use `^!`
	- `git diff 77e13ax^!`
- Compare specific directory
	- `git diff hash1 hash2 - path/to`
- See the number of changes
	- `git diff —stat hash1 hash2`
- See what in staged area
	- `git diff —staged`

## Reset
[version control - What's the difference between git reset --mixed, --soft, and --hard? - Stack Overflow](https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard)

## Squash
[git - How do I squash my last N commits together? - Stack Overflow](https://stackoverflow.com/questions/5189560/how-do-i-squash-my-last-n-commits-together)



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
	
### Pretty Print
`git ls-tree --full-tree --name-only -r HEAD`  
`git log --all --decorate --oneline --graph`

## Options
- `-C` run in specific directory `git -C ~/.SpaceVim pull`
- `-filter` 
- Save credential
	- `git config --global credential.helper store`
	- `git config credential.helper store`

## Command
- `hash-object` converts an existing file into a git object
- `cat-file` prints an existing git object to the standard output.

## Object
Now, **what actually is a Git object?** At its core, Git is a “content-addressed filesystem”. That means that unlike regular filesystems, where the name of a file is arbitrary and unrelated to that file’s contents, the names of files as stored by Git are mathematically derived from their contents. This has a very important implication: if a single byte of, say, a text file, changes, its internal name will change, too. To put it simply: you don’t _modify_ a file, you create a new file in a different location. Objects are just that: files in the git repository, whose path is determined by their contents.
- [[git submodule]]


___


[[Lazygit]]