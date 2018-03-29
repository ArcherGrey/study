# Async Hooks

模块提供了一个API用来注册追踪 `nodejs` 应用内创建的异步资源的生命周期的回调函数：
```
const async_hooks = require('async_hooks');
```

## `async_hooks.createHook(callbacks)`

`callbacks` 是需要注册的几个钩子回调函数：
- `init` 初始化资源
- `before` 在完成之前
- `after` 完成之后
- `destroy` 清除

需要追踪那个阶段就传入哪个参数，例如要只需要追踪资源回收：
```
const async_hooks = require('async_hooks');

const asyncHook = async_hooks.createHook({
  init(asyncId, type, triggerAsyncId, resource) { },
  destroy(asyncId) { }
});
```
