- [框架设计概述](#框架设计概述)
    - [设计目标](#设计目标)
- [一步步实现jQuery](#一步步实现jQuery)
    - [原型继承](#原型继承)
    - [返回实例](#返回实例)
    - [分隔作用域](#分隔作用域)
    - [跨域访问](#跨域访问)

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

# 一步步实现jQuery



## 原型继承

javascript中我们通过原型对象来实现面向对象的继承机制，也就是 `jQuery` 最基础的部分：
```
var jQuery = function(){} // 定义了最基础的jQuery类
jQuery.prototype = {
  // 扩展原型对象
}
jQuery.fn = jQuery.prototype = {
  // 使用一个新的名字
}

// 使用 $ 来指代 jQuery
var $ = jQuery = function(){}

```

## 返回实例

在通过原型继承的方式对 `jQuery` 添加了属性和方法之后，我们需要通过创建实例来调用它们：
```
// 一般实例化
var my$ = new $() // 创建实例
alter(my$.jquery) // 调用属性
alter(my$.size()) // 调用方法
```

但是 `jQuery` 并不是上面的样子，而是类似：
```
$().jquery;
$().size();
```

也就是把 `jQuery` 看作一个函数，返回值是 `jQuery` 类型的实例：
```
var $ = jQuery = function(){
  return new jQuery(); // 返回类的实例
}
```
但是这样写是不正确的，会出现无限循环，栈溢出。

所以，`jQuery` 使用了一个工厂方法来创建一个实例，把这个方法放在原型对象中，然后再函数中返回原型方法的调用：
```
var $ = jQuery = function(){
  return jQuery.fn.init(); // 调用原型方法 init()
}
jQuery.fn = jQuery.prototype = {
  init : function(){
    return this;
  },
  jquery : "123",
  size : function(){
    return this.length;
  }
}
alert($().jquery); // 调用属性，返回"123"
alert($().size()); // 调用方法，返回 undefined
```

## 分隔作用域

现在已经能够返回类的实例，我们把 `init()` 函数作为构造器，返回的 `this` 是对实例的引用，在 `init()` 内部初始化会用到 `this` 很容易破坏作用域的独立性，`jQuery` 是通过下面的方式来初始化构造函数：
```
var $ = jQuery = function(){
  return new jQuery.fn.init(); // 实例化init初始化类型，分隔作用域
}
```

这样就可以把构造函数内的 `this` 和 原型对象中的 `this` 分隔开来，避免相互混淆，但是这样做会带来另外一个问题：无法访问原型对象的属性或者方法。

## 跨域访问
如何实现既能分隔构造函数和原形对象的作用域，又能在实例中访问原型对象实现跨域访问呢？
`jQuery` 通过原型传递解决了这个问题，也就是通过`jQuery`的原型对象覆盖构造函数的原型对象，从而实现跨域访问：
```
var $ = jQuery = function(l){
  return new jQuery.fn.init(l);
}

jQuery.fn = jQuery.prototype = {
  init : function(l){  
    if(l!=undefined)
      this.length = l;
    this.test = function(){
      return this.length;
    }
    return this;
  },
  jquery : '123',
  length : 1,
  size : function(){
    return this.length;
  }
}

jQuery.fn.init.prototype = jQuery.fn; // 使用jQuery的原型对象来覆盖构造函数的原型对象
console.log($().jquery); // 返回 '123'
console.log($().length); // 返回1
console.log($(0).test()); // 返回0
console.log($(2).length); // 返回2
```
