# javascript 特殊技巧

## 求数组的最大最小
```
// es6 
var a=[1,5,2,5]
Math.min(...a) => Math.min(1,5,2,5) // 扩展运算符

// 最大类似，在 es5 中可以使用 apply 来代替
```

## 模板字符串

```
//es5 es6 最新的特性
var a=1;
var b= `it is ${a}` // 显示 it is 1
// 注意不是引号
```

