---
link: []
aliases: []
date created: Apr 8th, 2023
date modified: JulA2pr 19th, 2023
---

## Clear Git History
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

## rebase
- [git - How do I squash my last N commits together? - Stack Overflow](https://stackoverflow.com/questions/5189560/how-do-i-squash-my-last-n-commits-together)  
commit message was set after operation.

### Merge VS Rebase
- Merge the incoming changes into the current branch: select this option to perform [merge](http://schacon.github.io/git/git-merge.html) during the update. This is equivalent to running `git fetch` and then `git merge`, or `git pull --no-rebase`.
- Rebase the current branch on top of the incoming changes: select this option to perform [rebase](http://schacon.github.io/git/git-rebase.html) during the update. This is equivalent to running `git fetch` and then `git rebase`, or `git pull --rebase` (all local commits will be put on top of the updated upstream head).

## Pretty Print
`git ls-tree --full-tree --name-only -r HEAD`  
`git log --all --decorate --oneline --graph`

## Sparse Checkout
Used in mono repo.
> Reduce your working tree to a subset of tracked files

```
git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/cirosantilli/test-git-partial-clone

git sparse-checkout set --cone
git sparse-checkout set path/to/dir
```

- [Bring your monorepo down to size with sparse-checkout | The GitHub Blog](https://github.blog/2020-01-17-bring-your-monorepo-down-to-size-with-sparse-checkout/)

## Global `.gitignore`

```
git config --global core.excludesfile ~/.gitignore
```
