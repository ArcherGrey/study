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
- 注意，Buffer 模块会预分配一个大小为 Buffer.poolSize 的内部 Buffer 实例作为快速分配池， 用于使用 Buffer.allocUnsafe() 新创建的 Buffer 实例，以及废弃的 new Buffer(size) 构造器， 仅限于当 size 小于或等于 Buffer.poolSize >> 1 （Buffer.poolSize 除以2后的最大整数值）。
对这个预分配的内部内存池的使用，是调用 Buffer.alloc(size, fill) 和 Buffer.allocUnsafe(size).fill(fill) 的关键区别。 具体地说，Buffer.alloc(size, fill) 永远不会使用这个内部的 Buffer 池，但如果 size 小于或等于 Buffer.poolSize 的一半， Buffer.allocUnsafe(size).fill(fill) 会使用这个内部的 Buffer 池。 当应用程序需要 Buffer.allocUnsafe() 提供额外的性能时，这个细微的区别是非常重要的。(测试发现size大于Buffer.poolSize一半的时候两者的性能差距减小)
- Buffer.allocUnsafeSlow() 应当仅仅作为开发者已经在他们的应用程序中观察到过度的内存保留之后的终极手段使用
- [浅析buffer](https://cnodejs.org/topic/5189ff4f63e9f8a54207f60c)

