# 前言
其实很早之前就已经尝试过使用 Blogger 进行博客建设，但之前只是随意折腾了一下，如今打算正式整体迁移博客到 Blogger 中，主要是以下几点原因。

- 工作流的转变
    - 不再以 [Notion](https://www.notion.so/) 为中心，目前 Notion 只用于多人协作，看书数据库等内容
    - 开始使用 [简悦](https://simpread.pro/) 作为网页标注工具，同时配合自动化导出 Markdown 作为写文素材
    - 开始使用 [Obsidian](https://obsidian.md) 作为笔记软件
    - 发现了 [Stackedit.io](stackedit.io) 这个神器，能直接发布 Markdown 到 Blogger 中。配合 Dropbox 的同步，简直完美。
- 思维的转变
    - Local First!  云端软件只是获得了使用权，而不是所有权
        - 虽然用的 Blogger，所有文章本地储存+Dropbox 备份
    - Easy First! 随着学习压力的增大，愈发没有精力折腾各种乱七八糟的事了
- Blogger 本身质量过硬
    - 存活时间长
    - 安全性好
    - 访问速度快
    - 它的主题真的超棒，简洁大方(Essential Theme)，真的是换用 Blogger 的重要原因之一。

目前有了一个满意的工作流，不出意外应该不会折腾新工具了。
需要注意的是，需要自有域名才能让国内访问。

# 对比其他博客平台
优点
- 静态博客
    - 与 Vercel, Github pages 相比，Blogger 访问速度非常快(Google HK||TW Edge Node)
    - 开箱即用，不用装 Go || Nodejs
    - Blogger 主题真的超棒，真的符合审美
- Wordpress || Typecho
    - 快
    - 零成本
    - 稳
- 国内博客平台
    - 无需实名
    - 自定域名

缺点
- 改模板(会在文末给出 Github 地址直接抄)
    - 显示缩略图
    - 改 js css
    - 改评论
- 需要 Stackedit 才能支持 Markdown

# 步骤
## 1. 添加自定义域名
略，跟着步骤走，添加两个 CNMAE 记录即可，一个作为解析，一个作为认证（解析可以 A 记录到 `ghs.google.com` 于国内可用的 IP，访问较稳定）
开启 HTTPS 要等十分钟左右，在这之前是不能访问的，除非你关掉重定向，但记得之后重新打开，这时可以先修改模板。
## 2.修改模板
### 让博客正常访问
主要的工作就是将不能正常访问的文件换为可访问的直链。
这也意味着，以后图片都得使用图床，不能用 Blogger 内建的图片功能，不过我是用 Markdown 写作的，问题不大。
![在这里修改模板](https://s2.loli.net/2022/01/06/3zapZW1nUiHAL5M.png)

建议使用 Git 管理每一步更改，错了回退比较方便
Blogger 自带的模板编辑器还行，不过我是复制到 VSCode 下修改的
以 Essential 模板为例
- 下载 [链接](https://resources.blogblog.com/blogblog/data/res/2567166838-strm_compiled.js) 中的 JS 文件，修改其中的`src="https://www.blogger.com/img/blogger_logo_round_35.png"` ，换成可访问的直链（图床/OSS/Github）作为Favicon（网站图标）
- 搜索 `mspin_black_large.svg` 和 `mspin_white_large.svg` 和 `icon_delete13.gif` ，同样的，换成直链。
- 把末尾的 `<b:template-script async='true' name='strm' version='1.0.0'/>` 删掉换成上面修改过的文件（使用 GIthub+jsdelivr 或 OSS 托管 JS 文件）并添加 `<script async='async' src='https://YOU_DOMAIN.com/FILE_NAME.js'/>` 这行来调用 JS
- 将 `<head>` 替换为 `&lt;!--<head>--&gt;&lt;head&gt;`
- 将 `</head>` 替换为 `&lt;/head&gt;&lt;!--</head>--&gt;`
- 将 `<head>` 替换为 `&lt;!--</body>--&gt;&lt;/body&gt;`
---
做完上面那些，你的博客就能正常访问了，但加载时还是会转圈，此时还有问题的地方为评论和文章缩略图，先解决文章缩略图
### 文章缩略图显示
当文章中出现图片时（包括图床中的图片），Blogger 就会在首页生成缩略图，好东西，可惜被墙了。
为了让文章的缩略图能够正常显示，还需要为缩略图添加前置代理，使用的是 https://images.weserv.nl/ 的服务（类似于反向代理），操作如下
搜索 `<div class='snippet-thumbnail'>` ，将它下面那行替换成以下形式
```xml
<b:if cond='data:post.featuredImage'>
    <div class='snippet-thumbnail'>
        <img expr:src='"https://images.weserv.nl/?url=" + data:post.featuredImage'/> 
    </div>
</b:if>
```
对于 Essential 主题来说，一共有四处修改，改就行了
[原理见此](https://blog.iljw.me/2019/07/blogger-thumbnail.html)
插入一张图片，测试下，应该没问题了，有问题就说明没修改完全。
### 修复博客评论
非常感谢[这位博主](https://blogger.zhubin.org/2021/12/start-writing.html) 的帮助，完全抄自 Ta 的[方法](https://github.com/zhubinorg/blogger/blob/main/documents/disqusjs.md) ，这里简单复述下
1. 在 blogger 布局设置中添加一个新的 HTML/JavaScript 微件，标题和内容随意填写；
2. 在主题背景设置自定义下拉菜单选择修改 HTML，用你填写的标题内容找到相应代码块；
```xml
<b:widget id='HTML1' locked='false' title='微件标题' type='HTML' version='2' visible='true'>
<b:widget-settings>
<b:widget-setting name='content'>微件内容</b:widget-setting>
</b:widget-settings>
<b:includable id='main'>
此行加上下两行共三行就是你需要替换的内容
</b:includable>
</b:widget>
```
3. 将下面的内容修改后在合适的地方替换，保存后记得在布局设置中**启用**这个微件。
```xml
<b:includable id='main'>
<!-- jsDelivr -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/disqusjs@1.3/dist/disqusjs.css">
<script src="https://cdn.jsdelivr.net/npm/disqusjs@1.3/dist/disqus.js"></script>
<b:if cond='data:blog.pageType == "item"'>
<style type='text/css'>
#comments {display:none;}
</style>
<!-- shortname.disqus.com/blogger_item.js -->
<script>
(function () {
    "use strict";
    var get_comment_block = function () {
        var block = document.getElementById('comments');
        if (!block) {
            block = document.getElementById('disqus-blogger-comment-block');
        }
        return block;
    };
    var comment_block = get_comment_block();
    if (!!comment_block) {
        var disqus_div = document.createElement('div');
        disqus_div.id = 'disqus_thread';
        comment_block.innerHTML = '';
        comment_block.appendChild(disqus_div);
        comment_block.style.display = 'block';
        (document.getElementsByTagName('head')[0] || document.body).appendChild(dsq);
    }
})();</script>
<script>
var dsqjs = new DisqusJS({
    shortname: "自己填写",
    siteName: "",
    identifier: "<data:blog.url/>",
    url: "<data:blog.url/>",
    title: "",
    api: "https://disqus.skk.moe/disqus/详阅文档",
    apikey: "自己申请",
    admin: "",
    adminLabel: ""
});
</script>
</b:if>
<style type='text/css'>
.post-comment-link { visibility: hidden; }
</style>
</b:includable>
```
中间填写的内容请参考[这里](https://github.com/SukkaW/DisqusJS#%E4%BD%BF%E7%94%A8)  
`api` 可以填写本站的 `api endpoint` https://disqus.gaoji.fun/
___
至此，你的 Blogger 就能在大陆内正常访问了
可以参考[此 Google 知识库](https://support.google.com/blogger/answer/1233387) 添加裸域跳转等操作
# 参考资料
https://blogger.zhubin.org/2021/12/start-writing.html
https://blog.iljw.me/2019/07/blogger-thumbnail.html

<!--stackedit_data:
eyJwcm9wZXJ0aWVzIjoidGFnczogJ0Jsb2dnZXIsIOaKmOiFvi
dcbiIsImhpc3RvcnkiOlsyMDM4MDA5MTcsMTk0MjU0NjE3Ml19

-->