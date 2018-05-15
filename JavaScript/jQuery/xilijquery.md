- [框架设计概述](#框架设计概述)
    - [设计目标](#设计目标)
- [一步步实现jQuery](#一步步实现jQuery)
    - [原型继承](#原型继承)
    - [返回实例](#返回实例)
    - [分隔作用域](#分隔作用域)
    - [跨域访问](#跨域访问)
    - [选择器](#选择器)
    - [迭代器](#迭代器)
    - [功能扩展](#功能扩展)
    - [参数处理](#参数处理)
    - [名字空间](#名字空间)
- [深入了解选择器](#深入了解选择器)

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

## 选择器

`jQuery` 返回的是 `jQuery` 对象，是一个类数组的对象，也就是说它拥有数组的长度和下标，但是没有继承数组的方法。

`jQuery()` 函数包含两个参数 `selector` 和 `context` ，其中 `selector` 表示选择器，`context` 表示选择的内容范围，表示一个 `DOM` 元素：
```
var $ = jQuery = function(selector,context){
  return new jQuery.fn.init(selector,context); // 返回选择器实例
}
jQuery.fn = jQuery.prototype = {
  init: function(selector,context){
    selector = selector || document; // 默认为 document
    context = context || document; // 默认为 document
    if(selector.nodeType){ // 如果选择符为节点对象
      this[0] = selector; // 把参数节点传递给实例对象的数组
      this.length = 1;
      this.context = selector; // 设置实例的属性，返回选择范围
      return this;
    }
    if(typeof selector === 'string'){ // 如果选择符是字符串
      var e = context.getElementsByTagName(selector); // 获取指定名称的元素
      for(var i=0; i<e.length; i++){
        // 遍历元素集合，把所有元素填入到当前实例数组中
        this[i] = e[i];
      }
      this.length = e.length; // 设置实例的length属性，即定义包含的元素个数
      this.context = context; // 设置实例的属性，返回选择范围
      return this; // 返回当前实例
    }
    else{
      this.length = 0; // 就是没有选中的状态
      this.context = context; // 没有选中的时候属性就是 document
      return this;
    }
  },
  jQuery:1,
  size: function(){
    // 返回jQuery对象集合的长度
    return this.length;
  }
}
jQuery.fn.init.prototype = jQuery.fn;
```

## 迭代器

`jQuery` 对象有很多身份：
- 是一个数据集合，不是一个个体对象，无法直接使用 `javascript` 方法来操作
- 通过 `new` 创建的一个实例对象，和普通的对象一样，可以继承原型方法或属性，也拥有 `Object` 类型的方法和属性
- 包含数组特性，以数组结构存储返回的数据，是数组和对象的混合体，拥有数组结构但是没有数组方法，也就是说不是`Array` 类型，而是`Object` 类型:

```
var jquery = { // 定义对象直接量
  // 以属性方式存储信息
  name: "jQuery",
  value: 1
};
jquery[0] = "jQuery"; // 以数组方式存储信息
jquery[1] = 1;
```
- 对象包含的数据都是 `DOM` 元素，通过数组形式存储，通过类似数组下标`jQuery[n]` 的方式获取，还拥有类似数组长度的属性`length`，所以不能直接操作对象，只有分别读取包含的每一个`DOM`元素，才能实现各种操作

操作对象中`DOM` 元素的形式：
```
$('div').html();
```

> 具体实现

`jQuery` 定义了一个工具函数 `each()` ，利用这个工具就可以遍历对象中所有的`DOM`元素，并把需要操作的内容封装到一个回调函数中，然后通过在每个`DOM`元素上调用这个回调函数即可：
```
var $ = jQuery = function(selector,context){
  return new jQuery.fn.init(selector,context);
}
jQuery.fn = jQuery.prototype = {
  init: function(selector,context){
    // 省略。。和上面的一样
  },
  // 定义对象方法
  html: function(val){
    // 模仿jQuery中的html()方法，为匹配的每个DOM元素插入html代码
    jQuery.each(this,function(val){
      // 调用each工具函数为每个DOM元素执行回调函数
      this.innerHTML = val;
      },val)
  }
}
jQuery.fn.init.prototype = jQuery.fn;

// 扩展工具函数
jQuery.each = function(object,callback,args){
  for(var i=0; i<object.length; i++){
    callback.call(object[i],args);
  }
  return object;
}
$("div").html("测试代码");
```
上面的代码，通过先给`jQuery`对象绑定`html()`方法，然后利用选择器获取所有div元素，再调用`html()`方法为所有匹配的元素插入源码。

## 功能扩展

根据一般设计习惯，如果要给某个类添加函数或者方法，可以直接通过点语法实现。但是`jQuery`中是通过`extend()`函数来实现功能扩展的。

`extend()`函数能够方便用户快速扩展框架功能，但是不会破坏框架的原型结构，从而避免后期人工添加工具函数或者方法时破坏框架的单纯性，同时也方便管理。如果不需要某个插件，只需要简单地删除即可，而不需要在框架源代码中去筛选和删除。

`extend()`函数的功能实现起来也很简单，只是把指定对象的方法复制给`jQuery`对象或者`jQuery`原型对象：
```
var $ = jQuery = function(selector,context){
  return new jQuery.fn.init(selector,context);
}
jQuery.fn = jQuery.prototype = {
  init: function(selector,context){}
}
jQuery.fn.init.prototype = jQuery.fn;

// 扩展功能函数
jQuery.extend = jQuery.fn.extend = function(obj){
  for(var prop in obj){
    this[prop] = obj[prop];
  }
  return this;
}

// 扩展对象方法
jQuery.fn.extend({
  test: function(){
    console.log('测试扩展');
  }
})

// 测试代码
$('div').test();
```

## 参数处理

很多时候`jQuery`的方法都要求传递的参数为对象结构，使用对象直接量作为参数进行传递，方便参数管理。当方法或者函数的参数长度不固定时，使用对象直接量作为参数有很多优势。

使用对象直接量作为参数传递的载体，这里就涉及参数处理问题，解析并提取相应的参数：
```
var $ = jQuery = function(selector,context){
  return new jQuery.fn.init(selector,context);
}
jQuery.fn = jQuery.prototype = {
  init: function(selector,context){},
  setOptions: function(options){
    this.options = {
      // 方法的默认值，可以扩展
      a: 1,
      b: 2
    };
    jQuery.extend(this.options,options||{}); // 如果传递参数，就覆盖默认参数
  }
}
jQuery.fn.init.prototype = jQuery.fn;
jQuery.extend = jQuery.fn.extend = function(destination,source){
  // 重新定义
  for(var prop in source){
    destin[prop] = source[prop];
  }
  return destination;
}
```

上面的代码，定义了一个原型方法`setOptions`，该方法可以对传递的参数对象进行处理，并覆盖默认值。

`jQuery`框架中，`extend`既可以扩展方法，也可以处理参数对象，并覆盖默认值。

## 名字空间

到这里基本上已经有了框架的雏形，现在需要处理的问题就是名字空间冲突问题。

当一个页面中存在多个框架，或者代码量很大的时候，很难确保不会出现命名冲突，或者功能覆盖。为了解决这个问题，我们必须把框架封装在一个孤立的环境中，避免其他代码的干扰。

如果我们希望通过类似`$.method()`的方式来调用，就需要将`jQuery`设置为`window`对象的一个属性：
```
var jQuery = window.jQuery = window.$ = function(selector,context){
  return new jQuery.fn.init(selector,context);
}
```

`jQuery`框架希望和其他任何代码完全隔离开来，不暴露内部信息，也不允许其他代码随意访问，使用匿名函数就是一种最好的封闭方式。

到这里，框架的设计模式就初见端倪了，后面的工作就是根据应用需要或者功能需要进行扩展了。

# 深入了解选择器

`jQuery` 选择器功能强大，而且用法简单，它只提供了一个接口`jQuery()`或者简写`$()`。这一章我们深入分析选择器的设计思路、实现过程、工作原理。
