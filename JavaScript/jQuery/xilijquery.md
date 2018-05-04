- [框架设计概述](#框架设计概述)
    - [设计目标](#设计目标)     
- [技术栈](#技术栈)
    - [原型继承](#原型继承)
    - [](#返回实例)

# 框架设计概述
## 设计目标

`jQuery` = `javascript` + `Query` ，正如其名称一样，它的核心功能就是javascript 查询，更通俗的说就是选择DOM 元素，然后对元素进行操作。

框架最主要的两个功能就是： **选择 | 操作**


javascript 原生的DOM选择功能很有限，无法满足开发需求。所以根据css选择器和XPath选择器组成了jQuery选择器。

操作主要包括下面几个：
- 属性操作
- 元素操作
- 内容操作
- 样式操作
- 事件操作
- 通信操作

jQuery 的核心技术可以概括为：
- 选择
- 操作
- 扩展

# 技术栈

按照层次顺序

## 原型继承

javascript中我们通过原型对象来实现面向对象的继承机制：
```
var jQuery = function(){} // 定义了最基础的jQuery
jQuery.prototype = {
  // 扩展原型对象
}
jQuery.fn = jQuery.prototype = {
  // 使用一个新的名字
}

// 使用 $ 来指代 jQuery
var $ = jQuery = function(){}

```

##
