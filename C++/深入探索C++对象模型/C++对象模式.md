# C++对象模式
> C++有两种类数据成员：static 和 nonstatic；三种类成员函数：static,nonstatic,virtual

----------

## 简单对象模型(A Simple Object Model)

> 为了尽量降低C++编译器的设计复杂度而开发的，损失的是空间和执行效率。在这个模型中，一个对象是一系列的 `slots` （槽？），每个 `slot` 指向一个 `members` （包括数据成员和成员函数）。

如下图：简单对象模型

![](http://i.imgur.com/X7YS4DR.jpg)

在这个简单模型中，`members` 本身不放在对象中，只有指向 `members` 的指针才放在对象中（也就是 `slot`），这样可以避免因为成员的类型不同而需要不同的存储空间。

虽然这个模型没有应用于实际的产品中，不过关于 `slot` 的观念被应用到C++的指向成员的指针中去。


----------

## 表格驱动对象模型(A Tabel -driven Object Model)

> 这种对象模型是把所有与 `members` 相关的信息抽出来，放在一个数据成员表和成员函数表中，类对象本身则含有指向两个表格的指针，其中成员函数表示二级索引，首先是指向一系列 `slots`（成员函数表），然后是由一系列 `slots` 指向每个函数成员；而数据成员表示直接指向数据本身。

虽然这个模型也没有实际应用于真正的C++编译器上，但是成员函数表这个观念成为了虚函数的基础。


----------

# C++ 对象模型(The C++ Object Model)

> 最初的C++对象模型是由简单对象模型派生而来的，并对内存空间和存取时间做了优化。在此模型中，非静态数据成员被配置于类的每个对象之内，静态数据成员则被存放在所有的类对象之外，静态和非静态函数成员也被存放在所有的类对象之外。

虚函数则时由下面的步骤产生：

1. 每个类产生出一堆指向虚函数的指针，放在一个表格里，这个表格叫做虚表(virtual table)。
2. 每个类的对象被添加了一个指针，指向相关的虚表，一般这个指针被称为 `vptr`，这个指针的设定和重置都由每个类的构造、析构和拷贝自动完成的。每个类所关联的 `type_info object` 也是在虚表中，通常在表格的第一个位置(第一个slot)。


加上继承：



- 单一继承： `class a : public b {...};`
- 多重继承： `class a : public b,public c {...};`
- 继承关系还可以指定为虚拟的（virtual，也就是共享的意思）。虚继承的情况下，基类不管在继承串中被派生多少次，永远只会有一个实体。（如下图）

![](http://i.imgur.com/6uTT3ZQ.jpg)



