# event

大多数 `nodejs` 核心 `API` 都采用异步事件驱动，其中某些类型的对象（触发器）会周期性触发命名事件来调用函数对象（监听器）。

所有能触发事件的对象都是 `EventEmitter` 类实例。这些对象可以通过 `eventEmitter.on()` 将一个或多个函数绑定到会被对象触发的命名事件上。事件名称通常是驼峰命名的字符串，也可以使用任何有效的javascript属性名。
当 `EventEmitter` 对象触发一个事件时，所有绑定在该事件上的函数都被同步调用。

例子，一个绑定了监听器的 `EventEmitter` 实例，其中 `eventEmitter.on()`用于注册监听器，`eventEmitter.emit()`用于触发事件：
```
const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('触发了一个事件！');
});
myEmitter.emit('event');
```


