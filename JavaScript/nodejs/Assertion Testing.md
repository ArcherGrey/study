# 断言（Assert）

> `assert` 模块提供了一组简单的断言语句用来判断不变量

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
如果 `message` 为空，则会显示 `value == true`

---

## `assert.deepEqual(actual, expected[, message])`
如果 `actual` 和 `expected` 是原始类型（数字、字符串等等）那么就相当于 `actual == expected`。
如果是 `object` 类型，对象可枚举属性都相等的时候为真。
对于不可枚举的对象，例如正则表达式则不会抛出异常：
```
// WARNING: This does not throw an AssertionError!
assert.deepEqual(/a/gi, new Date());
```
`deep` 指的是可枚举对象的子对象也是可枚举而且相等的：
```
const assert = require('assert');

const obj1 = {
  a: {
    b: 1
  }
};
const obj2 = {
  a: {
    b: 2
  }
};
const obj3 = {
  a: {
    b: 1
  }
};
const obj4 = Object.create(obj1);

assert.deepEqual(obj1, obj1);
// OK, object is equal to itself

assert.deepEqual(obj1, obj2);
// AssertionError: { a: { b: 1 } } deepEqual { a: { b: 2 } }
// values of b are different

assert.deepEqual(obj1, obj3);
// OK, objects are equal

assert.deepEqual(obj1, obj4);
// AssertionError: { a: { b: 1 } } deepEqual {}
// Prototypes are ignored
```
如果不相等，`message` 和上面的一样

## `assert.deepStrictEqual(actual, expected[, message])`

严格相等：
```
const assert = require('assert');

assert.deepEqual({ a: 1 }, { a: '1' });
// OK, because 1 == '1'

assert.deepStrictEqual({ a: 1 }, { a: '1' });
// AssertionError: { a: 1 } deepStrictEqual { a: '1' }
// because 1 !== '1' using strict equality

// The following objects don't have own properties
const date = new Date();
const object = {};
const fakeDate = {};

Object.setPrototypeOf(fakeDate, Date.prototype);

assert.deepEqual(object, fakeDate);
// OK, doesn't check [[Prototype]]
assert.deepStrictEqual(object, fakeDate);
// AssertionError: {} deepStrictEqual Date {}
// Different [[Prototype]]

assert.deepEqual(date, fakeDate);
// OK, doesn't check type tags
assert.deepStrictEqual(date, fakeDate);
// AssertionError: 2017-03-11T14:25:31.849Z deepStrictEqual Date {}
// Different type tags

assert.deepStrictEqual(new Number(1), new Number(2));
// Fails because the wrapped number is unwrapped and compared as well.
assert.deepStrictEqual(new String('foo'), Object('foo'));
// OK because the object and the string are identical when unwrapped.
```

## assert.doesNotThrow(block[, error][, message])
