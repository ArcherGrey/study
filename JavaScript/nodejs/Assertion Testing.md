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

---

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

---

## `assert.doesNotThrow(block[, error][, message])`

当 `assert.doesNotThrow()` 被调用的时候，`block` 会立即调用。
如果抛出一个错误，并且它与 `error` 参数指定的类型相同，则抛出 `AssertionError`。 如果错误类型不同，或者错误参数未定义，则错误将传播回调用方。

```
assert.doesNotThrow(
  () => {
    throw new TypeError('Wrong value');
  },
  SyntaxError
);
```
会抛出 `typeError` 因为 `SyntaxError` 没有匹配

---

## `assert.equal(actual, expected[, message])`

和 `deepEqual` 的唯一区别在于，对于对象比较不相等：
```
assert.equal({ a: { b: 1 } }, { a: { b: 1 } });
//AssertionError: { a: { b: 1 } } == { a: { b: 1 } }
```
相等于对于每种类型的参数都做 `==` 操作

---

## `assert.fail(message) | assert.fail(actual, expected[, message[, operator[, stackStartFunction]]])`
`stackStartFunction` 例子：
```
function suppressFrame() {
  assert.fail('a', 'b', undefined, '!==', suppressFrame);
}
suppressFrame();
// AssertionError [ERR_ASSERTION]: 'a' !== 'b'
//     at repl:1:1
//     at ContextifyScript.Script.runInThisContext (vm.js:44:33)
//     ...
```

---

## `assert.ifError(value)`
```
const assert = require('assert');

assert.ifError(0);
// OK
assert.ifError(1);
// Throws 1
assert.ifError('error');
// Throws 'error'
assert.ifError(new Error());
// Throws Error
```
如果 `value` 为真，就抛出异常

---

## 注意事项

```
const a = 0;
const b = -a;
assert.notStrictEqual(a, b);
// AssertionError: 0 !== -0
// Strict Equality Comparison doesn't distinguish between -0 and +0...
assert(!Object.is(a, b));
// but Object.is() does!

const str1 = 'foo';
const str2 = 'foo';
assert.strictEqual(str1 / 1, str2 / 1);
// AssertionError: NaN === NaN
// Strict Equality Comparison can't be used to check NaN...
assert(Object.is(str1 / 1, str2 / 1));
// but Object.is() can!
```
Object.is() 判断两个值是否相同。如果下列任何一项成立，则两个值相同：

- 两个值都是 undefined
- 两个值都是 null
- 两个值都是 true 或者都是 false
- 两个值是由相同个数的字符按照相同的顺序组成的字符串
- 两个值指向同一个对象
- 两个值都是数字并且
- 都是正零 +0
- 都是负零 -0
- 都是 NaN
- 都是除零和 NaN 外的其它同一个数字

这种相等性判断逻辑和传统的 == 运算符所用的不同，== 运算符会对它两边的操作数做隐式类型转换（如果它们类型不同），然后才进行相等性比较，（所以才会有类似 "" == false 为 true 的现象），但 Object.is 不会做这种类型转换。

这与===运算符也不一样。===运算符（和==运算符）将数字值-0和+0视为相等，并认为Number.NaN不等于NaN。


