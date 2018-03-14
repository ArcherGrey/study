# 加载和运行

`<script>` 标签使得整个页面因为脚本解析、运行而出现等待，无论是内联还是包含在外边文件中的 javascript 代码，在`页面下载`和`解析过程`的时候都会使页面阻塞等待这些处理完成才能继续。

因为无法预知javascript是否会对页面进行修改，所以浏览器会停下来运行javascript然后继续解析翻译页面。这个过程中，页面解析和用户交互式被完全阻塞的。

## 脚本位置

`问题`：浏览器在遇到 `<body>` 标签的时候才会开始渲染，如果将脚本文件放在之前那么将会先下载运行脚本文件再进行渲染，这样做会使得其他页面资源被阻塞，也就是网页开始加载时用户必须等待一段空白页面直到脚本下载并且运行完成。

`解决`：推荐的办法是尽量将脚本文件放在 `<body>` 标签的底部位置，尽量减少对整个页面下载的影响。 

> 将脚本放在底部

## 脚本数量

`问题`：每个 `<script>` 标签下载时都会阻塞页面解析过程，下载一个100KB的文件比四个25KB的文件要快。（因为每个文件的下载都是http请求，文件数量多了请求数量也就多了）
`解决`：将多个脚本文件整个成一个文件，只使用一个标签引用，可以通过打包工具实现。

> 脚本文件越少越好

## 非阻塞脚本

`问题`：保持脚本文件短小，限制http请求数量，只是创建反应迅速的网页应用的第一步。一个应用程序所包含的功能越多所需要的javascript代码就越多，保持源码短小并不是总能实现。尽管下载一个大的javascript文件只产生一次请求，却会锁定浏览器一大段时间，为了解决这个问题我们需要向页面中逐步添加javascript，同时不阻塞浏览器。

`解决`：非阻塞脚本的秘密在于，等页面完成加载之后，再加载javascript。也就是说在页面 load 事件完成之后开始下载代码。

主要有下面几种方式实现：
- 延期脚本：html4 为 `<script>` 标签定义了一个扩展属性 `defer`。这个属性指明所包含的脚本不会修改DOM，因此代码可以稍后执行。这个方法需要 `Internet Explorer 4` 和 `Firefox 3.5` 更高版本的浏览器支持，如果浏览器支持的话，是一种可行的解决方案。带有扩展属性 `defer`的标签可以放在文档的任何位置。（经测试chrome不支持）

例子：(如果浏览器支持就会依次弹出“script”，“defer”和“load”，不支持会是“defer”，“script”和“load”)
```
<html>
<head>
<title>Script Defer Example</title>
</head>
<body>
<script defer>
alert("defer");
</script>
<script>
alert("script");
</script>
<script>
window.onload = function(){
alert("load");
};
</script>
</body>
</html>
```
<hr>

- 动态脚本节点（dynamic script node）：DOM允许你是用javascript动态创建几乎全部文档内容，`<script>` 和其他页面元素没有什么不同，所以可以使用DOM来动态加载javascript文件，这样加载代码使得代码的下载和运行都不会阻塞其他页面处理过程，而且还可以把动态加载的脚本放在页面的任何位置而不会对其余部分的页面代码造成影响。这种方法就能在页面中动态加载很多javascript文件，是非阻塞下载中最常用的模式，因为它可以跨浏览器同时简单易用。

例子：
```
var script = document.createElement ("script");
script.type = "text/javascript";
script.src = "file1.js";
document.getElementsByTagName_r("head")[0].appendChild(script);
```
<hr>

- XHR 脚本注入：这种方法首先创建一个XHR对象然后下载javascript文件，接着使用上面动态脚本加载的方法将代码注入页面。

例子：
```
var xhr = new XMLHttpRequest();
xhr.open("get", "file1.js", true);
xhr.onreadystatechange = function(){
if (xhr.readyState == 4){
if (xhr.status >= 200 && xhr.status < 300 || xhr.status == 304){
var script = document.createElement ("script");
script.type = "text/javascript";
script.text = xhr.responseText;
document.body.appendChild(script);
}
}
};
xhr.send(null);
```
此代码向服务器发送一个获取file1.js 文件的GET 请求。onreadystatechange 事件处理函数检查readyState是不是4，然后检查HTTP 状态码是不是有效（2XX 表示有效的回应，304 表示一个缓存响应）。如果收到了一个有效的响应，那么就创建一个新的<script>元素，将它的文本属性设置为从服务器接收到的responseText 字符串。这样做实际上会创建一个带有内联代码的<script>元素。一旦新<script>元素被添加到文档，代码将被执行，并准备使用。
  
这种方法的主要优点是，你可以下载javascript代码而不立即执行。由于代码返回在标签之外，所以下载后不会自动执行，可以人为控制执行时机。

不过这个方法有个限制：javascript文件必须与页面放置在同一个域内，正因为这个原因，大型网页通常不使用该技术。

## 推荐的非阻塞模式
 20
