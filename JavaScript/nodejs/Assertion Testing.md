# 断言（Assert）

> `assert` 模块提供了一组简单的断言语句用来测试

## `assert.ok(value[, message])` 

可以简写为 `assert(value[, message])`

例：
```
const assert = require('assert');

assert.ok(true);
// OK
assert.ok(1);
// OK
assert.ok(false);
// throws "AssertionError: false == true"
assert.ok(0);
// throws "AssertionError: 0 == true"
assert.ok(false, 'it\'s false');
// throws "AssertionError: it's false"
```
其中 `value` 为需要判断的表达式或者值，如果 `value` 的 结果为假则会抛出一个异常并显示 `message` 中的信息（`message` 选填）

--

## `assert.deepEqual(actual, expected[, message])`

