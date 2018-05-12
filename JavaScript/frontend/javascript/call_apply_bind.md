# call

`call` 也就是 `Function.prototype.call()` ，是函数类型特有的原型方法，可以传入一个指定的`this`和其他参数：
```
function Product(name, price) {
  this.name = name;
  this.price = price;
}

function Food(name, price) {
  Product.call(this, name, price);
  this.category = 'food';
}

console.log(new Food('cheese', 5).name);
// expected output: "cheese"
```

如果直接调用
