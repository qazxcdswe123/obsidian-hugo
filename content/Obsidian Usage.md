# Principle
1. 粒度足够小，每篇笔记只记录一个概念，最好给出例子
2. 不要前后文，能拆分出来自己独立成篇，能够独立理解，和其他的笔记没有依赖关系
3. 能够不加修改就能与原笔记相关联
4. 随意删除不会影响内容

# Plugins
- [[Excali Brain]]
	- Custom Shortcut `C-S-B`
- [GitHub - zolrath/obsidian-auto-link-title: Automatically fetch the titles of pasted links](https://github.com/zolrath/obsidian-auto-link-title)
	- Custom Shortcut `C-S-P`
- Templater
	- [[Hypotheis]]
- [GitHub - yuanotes/obsidian-vim-im-switch-plugin](https://github.com/yuanotes/obsidian-vim-im-switch-plugin)
	- 要删除 KeyboardHolder，换switchKey？
- [Index - Shell commands documentation - Obsidian Publish](https://publish.obsidian.md/shellcommands/Index)
	- `rsync -Pravh --delete Notes/ ~/code/hugo/content; git add -A; git -C ~/code/hugo commit -am "{{date:YYYY-MM-DD}}"; git -C ~/code/hugo push`
	- Custom Shortcut `C-S-G`
	
# Custom ShortCut
`Alt+W` Monthly Notes
`Alt+Q` Open Link
`Ctrl+G` Inline Code
`Ctrl+L` Toggle List

# Misc
[[yaml]] as front-matter