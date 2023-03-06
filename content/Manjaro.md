---
aliases: [Archlinux]
tags: [] 
date created: Jul 11th, 2022
date modified: Jan 7th, 2023
---
[[Linux]]

# System Customization
`echo 'blacklist pcspkr' | sudo tee --append /etc/modprobe.d/nobeep.conf` to get rid of the beep sound

# Custom Shortcut
1. `Super+W` = open browser
2. `Super+R` = open terminal
3. `Super+Shift+S` = screenshot

# 优点
`./program | xclip -selection c` copy output to clipboard  
Use [[ranger]] `yc` copy content `yn` copy name

# 问题
1. 微信 emoji 无法显示
2. `Ctrl+arrowKey` 无中文分词
3. scaling on HiDPI display
	1. [Matlab](https://ww2.mathworks.cn/matlabcentral/answers/406956-does-matlab-support-high-dpi-screens-on-linux)
	2. Gnome Tweak
	3. [依云blog](https://blog.lilydjwg.me/2022/2/2/wayfire-migration-4-not-so-high-dpi.216078.html)
4. Matlab mupad 无法输入中文
5. 鼠标滚轮速度调节 imwheel，但是触摸板就有问题了
6. Bluetooth 连接极慢 `sudo -e /etc/bluetooth/main.conf ` change setting
7. 鼠标速度有问题
8. 鼠标在 GTK 应用里会变大
9. White Color scheme with white text can't see
10. VSCode terminal font `"terminal.integrated.fontFamily": "MesloLGS NF"`
11. office kinda sucks
12. wayland fucked up after random upgrade, uninstall nvidia driver to fix, but screenshot fucked up after using wayland.

# 代理
1. 安装 Clash via pacman
	1. Config in `~/.config/clash/config.yaml`
2. create [[systemd]]

```
[Unit]
Description=Clash daemon
After=network.target

[Service]
Type=simple
Restart=always
MemoryLimit=125M
ExecStart=/usr/bin/clash -d /home/cyn/.config/clash

[Install]
WantedBy=multi-user.target
```

3. Set up proxy in network
4. Use [yacd](http://yacd.haishan.me/) to control clash
5. hope the program will use your proxy setting
6. [dns-over-https](https://blog.inetech.fun/Tutorial/dns-over-https-on-arch.html)

# 中文输入法
[方法](https://manateelazycat.github.io/linux/2020/06/19/fcitx5-is-awesome.html)  
完成后 logout

# Gnome

## Gnome Tweak
- 换主题
- 调缩放

## Gnome Box
work out of the box

## Gnome Terminal
`gnome-terminal --window --maximize` add to custom shortcut with `Super+R`

## Add Desktop Icon
[Unix Exchange](https://unix.stackexchange.com/questions/103213/how-can-i-add-an-application-to-the-gnome-application-menu)  
`~/.local/share/applications/`

# 软件
`sudo yay install obsidian-appimage dropbox picgo-appimage `
- Dropbox works perfectly
- WeChat
	- 解决中文显示问题
		- [GitHub](https://github.com/vufa/deepin-wine-wechat-arch#%E4%B8%AD%E6%96%87%E5%AD%97%E4%BD%93%E6%98%BE%E7%A4%BA%E4%B8%BA%E6%96%B9%E6%A1%86%E6%98%BE%E7%A4%BA%E6%A8%A1%E7%B3%8A)
		- [Blog](https://www.danielw7.com/ubuntu20-04-%E5%AE%89%E8%A3%85%E5%BE%AE%E4%BF%A1-%E8%A7%A3%E5%86%B3%E4%B8%AD%E6%96%87%E6%98%BE%E7%A4%BA%E9%97%AE%E9%A2%98/)
	- 解决缩放问题
		- `~/.pam_environment` 
		- `WINEPREFIX=~/.deepinwine/Deepin-WeChat deepin-wine6-stable winecfg`
- fzf
	- [[Linux Command Modern Alternative]]
	- It's kind of magic
- [[ranger]] [[Vim]]
- [[Vim]]
- [Flameshot](https://github.com/flameshot-org/flameshot)
- [[VSCode]]
- [[Color Scheme]]
- [[Command Line]]

# 总结
上了 [[Linux]] 就知道 Windows 下的字体渲染和编程体验是多么的屎  
同时也知道 [[Linux]] 是有多折腾，Out of the box experience? tan90