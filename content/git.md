# git
## commit
附加修改提交信息
`git commit --amend "foobar"`

## clear git history
1.  Checkout
    `git checkout --orphan latest_branch`
2.  Add all the files
    `git add -A`
3.  Commit the changes
    `git commit -am "commit message"`
4.  Delete the branch
    `git branch -D main`
5.  Rename the current branch to main
    `git branch -m main`
6.  Finally, force update your repository
    `git push -f origin main`

## options
- `-C` run in specific directory `git -C ~/.SpaceVim pull`
- `git config --global credential.helper store`
- `git config credential.helper store`


- [[git submodule]]


## Hack
`git ls-tree --full-tree --name-only -r HEAD`

___


# lazygit
[[02-Vim]]
**2. 文件面板**
- `A` = amend 添加到上一次更改
- `P` = push
- `p` = pull
- `d` = 放弃/删除

- `s` = 隐藏/stash [stash use case](https://stackoverflow.com/questions/20537223/what-is-the-intended-use-case-for-git-stash)
- `g` = pop 一次 stash

- `<SPACE>` = add/unadd
- `<Tab>` = switch
**3. 分支面板**
- `n` = new branch
- `<SPCAE>` = select branch
- `M` = 选中分支合并到当前分支（合并两个分支）
- `[ ]` = 翻页
- `d` = 删除分支
- `M` = 合并 Merge
- 	`<Enter>` = 进入 conflict
- 	`<SPCAE>` = 选择需要的更改
  

**4. 提交面板**
- `<Enter>` = 查看提交文件
- `, .` = 翻页
- `< >` = 到最顶端最底端
- `/` = 搜索 Commit msg
- `r` = 更改提交信息
- `<SPACE>` = checkout
- `g` = reset 重置
	- soft reset 删除 commit 但不删除更改
	- hard reset 更改
	- **可以在 reflog 上reset 撤销**
- `[ ]` = 翻页
- `d` = 删除提交
- `<C-s>` = filter 提交
- `W` = diff Mode

- `s` = 选中的提交和下面一个提交合并(squash)
- `f` = 选中的提交和下面一个提交合并(fixup)
	- squash 会合并信息
	- fixup 不会合并信息
- `e` = 批量 **sf**+(**d**)rop+(**p**)ick 批量修改 commit

- cherry-pick
	- `c` = 选择（复制）提交
	- `v` = 粘贴到所选分支

patch
[Video](https://www.bilibili.com/video/BV1gV411k7fC)