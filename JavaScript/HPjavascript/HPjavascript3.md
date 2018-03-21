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

当浏览器下载完成所有页面html标记、javascript、css、图片之后，会解析文件并且创建两个内部数据结构：
- DOM 树：表示页面结构
- 渲染树：表示DOM节点如何显示

渲染树中为每个需要显示的DOM树节点存放至少一个节点（隐藏的DOM元素在渲染树中没有对应节点）。渲染树上的节点称为框或者盒，符合css模型定义，将页面元素看成一个具有填充、边距、边框和位置的盒。一旦DOM树和渲染树构造完毕，浏览器就可以显示（绘制）页面上的元素了。

当DOM改变影响到元素的几何属性导致其他元素的几何属性和位置受到影响，浏览器使渲染树上受到影响的部分失效，然后重构渲染树。这个过程称为重排版。重排版完成时，浏览器在一个重绘进程中重新绘制屏幕上受影响的部分。

不是所有的DOM 改变都会影响几何属性。例如，改变一个元素的背景颜色不会影响它的宽度或高度。在这种情况下，只需要重绘（不需要重排版），因为元素的布局没有改变。

重绘和重排版是负担很重的操作，可能导致网页应用的用户界面失去相应。所以，十分有必要尽可能减少这类事情的发生。

### 重排版
当布局和几何改变时需要重排版。在下述情况中会发生重排版：
- 添加或删除可见的DOM 元素
- 元素位置改变
- 元素尺寸改变（因为边距，填充，边框宽度，宽度，高度等属性改变）
- 内容改变，例如，文本改变或图片被另一个不同尺寸的所替代
- 最初的页面渲染
- 浏览器窗口改变尺寸

根据改变的性质，渲染树上或大或小的一部分需要重新计算。某些改变可导致重排版整个页面：例如，当一个滚动条出现时。

### 查询并刷新渲染树改变

因为计算量与每次重排版有关，大多数浏览器通过队列化修改和批量显示优化重排版过程。然而，你可能（经常不由自主地）强迫队列刷新并要求所有计划改变的部分立刻应用。获取布局信息的操作将导致刷新队列动作，这意味着使用了下面这些方法：
- offsetTop, offsetLeft, offsetWidth, offsetHeight
- scrollTop, scrollLeft, scrollWidth, scrollHeight
- clientTop, clientLeft, clientWidth, clientHeight
- getComputedStyle()

布局信息由这些属性和方法返回最新的数据，所以浏览器不得不运行渲染队列中待改变的项目并重新排版以返回正确的值。

在改变风格的过程中，最好不要使用前面列出的那些属性。任何一个访问都将刷新渲染队列，即使你正在获取那些最近未发生改变的或者与最新的改变无关的布局信息。

### 最小化重绘和重排版
重排版和重绘代价昂贵，所以，提高程序响应速度一个好策略是减少此类操作发生的机会。为减少发生次数，你应该将多个DOM 和风格改变合并到一个批次中一次性执行。

### 缓冲布局信息

浏览器通过队列化修改和批量运行的方法，尽量减少重排版次数。当你查询布局信息如偏移量、滚动条位置，或风格属性时，浏览器刷队列并执行所有修改操作，以返回最新的数值。最好是尽量减少对布局信息的查询次数，查询时将它赋给局部变量，并用局部变量参与计算。

### 将元素提出动画流
显示和隐藏部分页面构成展开/折叠动画是一种常见的交互模式。它通常包括区域扩大的几何动画，将页面其他部分推向下方。
重排版有时只影响渲染树的一小部分，但也可以影响很大的一部分，甚至整个渲染树。浏览器需要重排版的部分越小，应用程序的响应速度就越快。所以当一个页面顶部的动画推移了差不多整个页面时，将引发巨大的重排版动作，使用户感到动画卡顿。渲染树的大多数节点需要被重新计算，它变得更糟糕。

使用以下步骤可以避免对大部分页面进行重排版：
- 使用绝对坐标定位页面动画的元素，使它位于页面布局流之外。
- 启动元素动画。当它扩大时，它临时覆盖部分页面。这是一个重绘过程，但只影响页面的一小部分，避免重排版并重绘一大块页面。
- 当动画结束时，重新定位，从而只一次下移文档其他元素的位置。

> 译者注：文字描述比较简单概要，我对这三步的理解如下：
>1. 页面顶部可以“折叠/展开”的元素称作“动画元素”，用绝对坐标对它进行定位，当它的尺寸改变时，就
不会推移页面中其他元素的位置，而只是覆盖其他元素。
>2. 展开动作只在“动画元素”上进行。这时其他元素的坐标并没有改变，换句话说，其他元素并没有因为“动
画元素”的扩大而随之下移，而是任由动画元素覆盖。
>3. “动画元素”的动画结束时，将其他元素的位置下移到动画元素下方，界面“跳”了一下。

## 事件托管
当页面中存在大量元素，而且每个元素有一个或多个事件句柄与之挂接（例如onclick）时，可能会影响性能。连接每个句柄都是有代价的，无论其形式是加重了页面负担（更多的页面标记和JavaScript 代码）还是表现在运行期的运行时间上。你需要访问和修改更多的DOM 节点，程序就会更慢，特别是因为事件挂接过程都发生在onload（或DOMContentReady）事件中，对任何一个富交互网页来说那都是一个繁忙的时间段。挂接事件占用了处理时间，另外，浏览器需要保存每个句柄的记录，占用更多内存。当这些工作结束时，这些事件句柄中的相当一部分根本不需要（因为并不是100%的按钮或者链接都会被用户点到），所以很多工作都是不必要的。


一个简单而优雅的处理DOM 事件的技术是事件托管。它基于这样一个事实：事件逐层冒泡总能被父元素捕获。采用事件托管技术之后，你只需要在一个包装元素上挂接一个句柄，用于处理子元素发生的所有事件。

根据DOM 标准，每个事件有三个阶段：
- 捕获
- 到达目标
- 冒泡


例子：
```
<html>
	<head>
		<body>
			<div>
				<ul id='menu'>
					<li>
						<a href="menu1.html">menu1 #1</a>
					</li>
					<li></li>
					<li></li>
				</ul>
			</div>
		</body>
	</head>
</html>
```

当用户点击了 `menu1 #1` 链接，点击事件首先被 <a> 元素收到，然后沿着DOM树冒泡，被 <li> 元素收到，然后是 <ul> ，接着是 <div> 等等，一直到达文档的顶层，甚至WINDOW，这使得你可以只在父元素上挂接一个事件句柄，来接收所有子元素产生的事件通知。

事件托管技术并不复杂，你只需要监听事件，看看他们是不是从你感兴趣的元素中发出的。这里有一些冗余的跨浏览器代码，如果你将它们移入一个可重用的库中，代码就变得相当干净。
跨浏览器部分包括：
- 访问事件对象，判断事件源
- 结束文档树上的冒泡
- 阻止默认动作

## 总结

DOM 访问和操作是现代网页应用中很重要的一部分。但每次你通过桥梁从ECMAScript 岛到达DOM 岛时，都会被收取“过桥费”。为减少DOM 编程中的性能损失，请牢记以下几点：
- 最小化DOM 访问，在JavaScript 端做尽可能多的事情
- 在反复访问的地方使用局部变量存放DOM 引用
- 小心地处理HTML 集合，因为他们表现出“存在性”，总是对底层文档重新查询。将集合的length 属性缓存到一个变量中，在迭代中使用这个变量。如果经常操作这个集合，可以将集合拷贝到数组中
- 如果可能的话，使用速度更快的API，诸如querySelectorAll()和firstElementChild
- 注意重绘和重排版；批量修改风格，离线操作DOM 树，缓存并减少对布局信息的访问
- 动画中使用绝对坐标，使用拖放代理
- 使用事件托管技术最小化事件句柄数量