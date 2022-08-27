---
aliases: []
tags: [] 
date created: Jul 21st, 2022
date modified: Aug 15th, 2022
---
## Softwere
### Microsoft
- Onedrive
- Word
- Powerpoint
- Excel

### App Store
- ScanScan
- GoodNotes
- Telegram
- Tencent Meeting
- feishu
- [[marginnote]]


### Homebrew
- Formula: 命令行软件
- Cask: GUI 软件
- Bottle: 预编译软件

- `brew autoremove` to uninstall dependencies  
[Homebrew 源使用帮助 — USTC Mirror Help 文档](https://mirrors.ustc.edu.cn/help/brew.git.html)
- Cask
	- AlDente (Charge Limit)
	- syntax-highlight  (For Quick Preview via `Space`)
	- Motrix (Aria2 GUI)
	- Obsidian (note)
	- [[iterm2]] (terminal alternative)
	- unnaturalscrollwheels
	- google-chrome
	- visual-studio-code (ide)
	- discord
	- calibre (book manager)
	- raycast (launcher)
	- dash (document viewer)
	- keka (zip tool)
	
	- orion

- Formula
	- jq
	- bash
	- rust
	- yadm
	- [[neovim]]
	- [[ripgrep]]
	- htop
	- [[python]]
	- [[NodeJS Package Manager|pnpm]] 
	- [[NodeJS]]
	- wget
	- fd
	- lazygit + [[git]]
	- dust
	- fzf
	- [[ranger]]
	- trash
	- tldr
	- bat
	- go
	- [[hugo]]
	- firacode ([[Font]])
	- java
		- `echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc`

### Manual Download
- [ClashX Pro](https://install.appcenter.ms/users/clashx/apps/clashx-pro/distribution_groups/public) (proxy)
- [Releases · Molunerfinn/PicGo · GitHub](https://github.com/Molunerfinn/PicGo/releases) (M1 Support)
- [KeyboardHolder](https://keyboardholder.leavesc.com/en-us/) (Control your input method)

## Hack

```
defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false         # For VS Code
defaults write com.microsoft.VSCodeInsiders ApplePressAndHoldEnabled -bool false # For VS Code Insider
defaults write com.visualstudio.code.oss ApplePressAndHoldEnabled -bool false    # For VS Codium
defaults delete -g ApplePressAndHoldEnabled # restore to default (not including 3 above)
```

- configure [[VSCode]] [[font]]  
`"terminal.integrated.fontFamily": "FiraCodeNerdFontCompleteM-Retina"`

- Edit `/etc/shells`  
`/opt/homebrew/bin/bash`

- Edit `/etc/ssh/ssh_config`
```
ServerAliveInterval 20
ServerAliveCountMax 999

# or
echo "ServerAliveInterval 20
ServerAliveCountMax 999
" >> /etc/ssh/ssh_config
```


## System Preference
- Automatically Hide Menu-bar and Dock
	- Smaller Size
- Show battery percentage
- trackpad:
	- fastest
	- tap to click
- [macos - Using Caps Lock as Esc in Mac OS X - Stack Overflow](https://stackoverflow.com/questions/127591/using-caps-lock-as-esc-in-mac-os-x)
- Uncheck `play sound on startup` && `play UI sound effect`


## Shortcut
- `Shift+CMD+5`: screenShot
- `CMD+,`: Open Preference
- `Command + Shift + Z`: look up word
- press `Control` and click to act as right click
- `CMD+Shift+R`: Enter reader mode
- Dictionary
	- `CMD+Control+D`: Lookup
	- `CMD+Shift+X`: Open Dictionary
- Screenshot
	- `Shift+CMD+3`: Fullscreen screenshot 
	- `Shift+CMD+4`: Portion screenshot
	- `Shift+CMD+4+SpaceBar`: Select window screenshot
- ![](https://img.ynchen.me/2022/07/1ee4ed251c07ded5b5da043191d02497.png)


### Terminal
[[Shell]]  
Preferences > Profiles > Keys > Load Presets not Preferences > Keys > Load Preferences > Natrual
