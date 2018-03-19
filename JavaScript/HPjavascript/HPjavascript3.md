# DOM 编程

对DOM操作的代价昂贵，通常是一个性能瓶颈。主要有三个方面：
- 访问和修改DOM元素
- 修改DOM元素的样式，造成重绘和重新排版
- 通过DOM事件处理用户响应

## DOM为什么会慢？
DOM和javascript实现保持相互独立。两个独立的部分通过功能接口连接就会带来性能损耗。

DOM是一个岛，javascript是一个岛，每次javascript访问DOM需要过桥，交一次过桥费，所以操作DOM次数越多，费用就越高。

## DOM 访问和修改
访问DOM就是交一次过桥费，修改DOM的费用可能更高，因为它可能导致浏览器重新计算页面变化。

最坏情况是使用在循环中执行这些操作。

### innerHTML和DOM方法

两者性能差距不大，不过在老式浏览器中，innerHTML速度更快一点，在最新的基于WebKit的浏览器（chrome和Safari）正相反。

### 节点克隆

使用DOM方法更新页面内容的另一个途径是克隆节点 ——— `element.cloneNode()` 代替 `document.createElement()`

在大多数浏览器中，克隆节点更有效率，但是提高不多：
- IE8 快2% IE6 和 IE7 没有变化
- Firefox 3.5 和 Safari 4 快了5.5%
- opera 快了 6%
- chrome2 快了10% chrome3 快了3%

### HTML集合
HTML 集合实际上在查询文档，当你更新信息时，每次都要重复执行这种查询操作。例如读取集合中元素的数目（也就是集合的length）。这正是低效率的来源。

例子：
```
var alldivs = document.getElementsByTagName_r('div');
for (var i = 0; i < alldivs.length; i++) {
document.body.appendChild(document.createElement('div'))
}
```
这段代码看上去只是简单地倍增了页面中div 元素的数量。它遍历现有div，每次创建一个新的div 并附加到body 上面。但实际上这是个死循环，因为循环终止条件alldivs.length 在每次迭代中都会增加，它反映出底层文档的当前状态。

像这样遍历HTML 集合会导致逻辑错误，而且也很慢，因为每次迭代都进行查询。

优化的办法很简单，只要将集合的length 属性缓存到一个变量中，然后在循环判断条件中使用这个变量。

## DOM API

你经常需要从一个DOM 元素开始，操作周围的元素，或者递归迭代所有的子节点。你可以使用childNode集合或者使用nextSibling 获得每个元素的兄弟节点。
在不同浏览器上，这两种方法的运行时间基本相等。但是在IE 中，nextSibling 表现得比childNode 好。在IE6 中，nextSibling 比对手快16 倍，而在IE7 中快105 倍。鉴于这些结果，在老的IE 中性能严苛的使用条件下，用nextSibling 抓取DOM 是首选方法。在其他情况下，主要看个人和团队偏好。

## 重绘和重排版

85
