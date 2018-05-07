# this
在面向对象语言中，代表了当前对象的一个引用，但是在 `javascript` 中会随着它的执行环境的改变而改变。

`javascript` 中 `this` 总是指向调用它所在方法的对象，因为 `this` 是在函数运行时自动生成的一个内部对象，只能在函数内部使用。

分下面几种情况具体分析：

> 全局的函数调用

```
var name = 'test';
function a(){
  console.log(this==window); 
  console.log(this.name); 
}
a(); // true test
```

在全局函数中的 `this` 就代表全局对象 `window` ，也就是说 `this` 指向的是调用方法所在的对象

---

> 对象方法的调用

```
function showname(){
  console.log(this.name);
}
var obj = {};
obj.name = 'test';
obj.show = showname;
obj.show(); // test
```

如果函数作为对象的方法调用，`this` 指向的还是调用方法的对象

---

> 构造函数的调用

```
function showname(){
  this.name = 'test';
}
var obj = new showname();
console.log(obj.name); // test
```

构造函数中的 `this` 指向的是通过该构造函数创建的对象的实例

---

> apply/call

apply和call都是为了改变函数体内部的this指向。 其具体的定义如下：
call方法:
语法：call(thisObj，Object)
定义：调用一个对象的一个方法，以另一个对象替换当前对象。
说明：
call 方法可以用来代替另一个对象调用一个方法。call 方法可将一个函数的对象上下文从初始的上下文改变为由 thisObj 指定的新对象。
如果没有提供 thisObj 参数，那么 Global 对象被用作 thisObj。

apply方法:
语法：apply(thisObj，[argArray])
定义：应用某一对象的一个方法，用另一个对象替换当前对象。
说明：
如果 argArray 不是一个有效的数组或者不是 arguments 对象，那么将导致一个 TypeError。
如果没有提供 argArray 和 thisObj 任何一个参数，那么 Global 对象将被用作 thisObj， 并且无法被传递任何参数。

```
var value = "Global value";

    function FunA() {
        this.value = "AAA";
    }

    function FunB() {
        console.log(this.value);
    }
    FunB(); //Global value 因为是在全局中调用的FunB(),this.value指向全局的value
    FunB.call(window); //Global value,this指向window对象，因此this.value指向全局的value
    FunB.call(new FunA()); //AAA, this指向参数new FunA()，即FunA对象

    FunB.apply(window); //Global value
    FunB.apply(new FunA()); //AAA
```
在上述代码中，this的指向在call和apply中是一致的，只不过是调用参数的形式不一样。call是一个一个调用参数，而apply是调用一个数组。
