# buffer 
- `alloc` 比 `allocUnsafe`慢，但是`allocUnsafe`可能有旧数据，需要先初始化。（测试证明使用 `allocUnsafe`然后再用`buff.fill`初始化的总时间都比 `alloc` 快很多）
- 如果 `size` 小于或等于 `Buffer.poolSize` 的一半，则 `Buffer.allocUnsafe()` 返回的 `Buffer` 实例可能会被分配进一个共享的内部内存池。
- `Buffer` 实例可以使用 `ECMAScript 2015 (ES6)` 的 `for..of` 语法进行遍历:
```
const buf = Buffer.from([1, 2, 3]);

// 输出:
//   1
//   2
//   3
for (const b of buf) {
  console.log(b);
}
```

