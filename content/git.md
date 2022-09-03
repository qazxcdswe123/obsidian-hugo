---
aliases: []
tags: [] 
date created: Jul 13th, 2022
date modified: Sep 2nd, 2022
---
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
```

___
[Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- `git config --global credential.helper store`

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
	
### Pretty Print
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