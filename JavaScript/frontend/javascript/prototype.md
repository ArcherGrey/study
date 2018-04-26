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

几乎所有函数都有 `prototype` 属性，这个属性就是一个指针，指向一个对象~~原型对象？~~，对象包含所有实例共享的属性和方法。

每个对象~~非基础类型~~都具有 `__proto__` ，也可以称为隐式原型，也是一个指针，指向构造对象的构造函数的原型:
```
var a={} // a 是一个 Object 实例
console.log(a.__proto__ == Object.prototype) // a 的 __proto__ 指向 a 的构造函数的原型对象，a 是由 Object 构造的，Object.prototype 是Object的原型对象，所以两者相等
```


## 继承

每个对象都有一个私有属性 `[Prototype]` ~~也就是`.__proto__`~~ ，指向它的原型对象 `prototype`，该 `prototype`对象又具有一个自己的`prototype`，层层向上直到一个对象的原型为 `null`。`null` 没有原型，是原型链的最后一环。

javascript 对象有一个指向一个原型对象的链，当试图访问一个的对象的属性的时候，不仅仅会在该对象上搜寻，还会搜寻该对象的原型，以及该对象的原型的原型，层层向上搜索~~深度搜索~~，直到找到一个名字匹配的属性或者到达原型链的末尾~~null~~。

看一个例子：
```
// 让我们假设我们有一个对象 o, 其有自己的属性 a 和 b：
// {a: 1, b: 2}
// o 的 [[Prototype]] 有属性 b 和 c：
// {b: 3, c: 4}
// 最后, o.[[Prototype]].[[Prototype]] 是 null.
// 这就是原型链的末尾，即 null，
// 根据定义，null 没有[[Prototype]].
// 综上，整个原型链如下: 
// {a:1, b:2} ---> {b:3, c:4} ---> null

console.log(o.a); // 1
// a是o的自身属性吗？是的，该属性的值为1

console.log(o.b); // 2
// b是o的自身属性吗？是的，该属性的值为2
// 原型上也有一个'b'属性,但是它不会被访问到.这种情况称为"属性遮蔽 (property shadowing)"

console.log(o.c); // 4
// c是o的自身属性吗？不是，那看看原型上有没有
// c是o.[[Prototype]]的属性吗？是的，该属性的值为4

console.log(o.d); // undefined
// d是o的自身属性吗？不是,那看看原型上有没有
// d是o.[[Prototype]]的属性吗？不是，那看看它的原型上有没有
// o.[[Prototype]].[[Prototype]] 为 null，停止搜索
// 没有d属性，返回undefined
```

javascript 没有其他基于类的语言所定义的方法，任何函数都可以添加到对象上作为对象的属性，函数的继承和其他属性的继承没有差别，包括上面的属性遮蔽。

当继承的函数被调用的时候， `this` 指向的是当前继承的对象，而不是继承的函数所在的原型对象：
```
var o = {
  a: 2,
  m: function(){
    return this.a + 1;
  }
};

console.log(o.m()); // 3
// 当调用 o.m 时,'this'指向了o.

var p = Object.create(o);
// p是一个继承自 o 的对象

p.a = 4; // 创建 p 的自身属性 a
console.log(p.m()); // 5
// 调用 p.m 时, 'this'指向 p. 
// 又因为 p 继承 o 的 m 函数
// 此时的'this.a' 即 p.a，即 p 的自身属性 'a'
```

## 使用不同的方法创建和生成原型链

> 语法结构创建的对象

```
var o = {a: 1};

// o 这个对象继承了Object.prototype上面的所有属性
// o 自身没有名为 hasOwnProperty 的属性
// hasOwnProperty 是 Object.prototype 的属性
// 因此 o 继承了 Object.prototype 的 hasOwnProperty
// Object.prototype 的原型为 null
// 原型链如下:
// o ---> Object.prototype ---> null

var a = ["yo", "whadup", "?"];

// 数组都继承于 Array.prototype 
// (Array.prototype 中包含 indexOf, forEach等方法)
// 原型链如下:
// a ---> Array.prototype ---> Object.prototype ---> null

function f(){
  return 2;
}

// 函数都继承于Function.prototype
// (Function.prototype 中包含 call, bind等方法)
// 原型链如下:
// f ---> Function.prototype ---> Object.prototype ---> null
```
