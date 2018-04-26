# 原型链

> `javascript` 常被描述为一种 **基于原型（prototype-based language）** 的语言。每个对象都拥有一个 **原型对象** ，对象以原型为模板、从原型继承方法和属性。原型对象也可能拥有原型，并从中继承方法和属性，一层一层，这种关系常被称为 **原型链** 。

准确的说，这些属性和方法定义在 `Object` 的构造函数上的 `prototype` 属性上，而非对象实例本身：
```
var a = {} // a 是一个对象实例
console.log(a.prototype) // undefined 
var b = function (){} // b 是一个函数
console.log(b.prototype) // 不是undefined ，应该是b 可以看作构造函数
```
## `prototype` 和 `__proto__`

- 几乎所有函数都有 `prototype` 属性，这个属性就是一个指针，指向一个对象~~原型对象？~~，对象包含所有实例共享的属性和方法
- 每个对象~~非基础类型~~都具有 `__proto__` ，也可以称为隐式原型，也是一个指针，指向构造对象的构造函数的原型:
```
var a={} // a 是一个 Object 实例
console.log(a.__proto__ == Object.prototype) // a 的 __proto__ 指向 a 的构造函数的原型对象，a 是由 Object 构造的，Object.prototype 是Object的原型对象，所以两者相等
```

