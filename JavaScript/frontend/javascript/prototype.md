# 对象原型（prototype）~~叫原型对象好像也行~~

`javascript` 常被描述为一种 **基于原型（prototype-based language）** 的语言。

几乎所有的 `javascript` 对象都是 `Object` 实例，每个对象都拥有一个 **原型对象** ，对象以原型为模板、从原型继承方法和属性。

原型对象也可能拥有原型，并从中继承方法和属性，一层一层，这种关系常被称为 **原型链** 。

准确的说，这些属性和方法定义在 `Object` 的构造函数上的 `prototype` 属性上，而非对象实例本身：
```
var a = {} // a 是一个对象实例
console.log(a.prototype) // undefined 
var b = function (){} // b 是一个函数
console.log(b.prototype) // 不是undefined ，应该是b 可以看作构造函数
```


