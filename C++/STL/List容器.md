# List容器
> List使用双向链表来存储元素

使用List时必须导入头文件

    #include<list>

List类型定义于namespace std中，是个模板类(和vector一样)：

    namespace std{
    	template <class T, class Allocator = allocator<T> >
    	class list;
    }

## List的特点
List的内部结构和vector或deque完全不同，在下面几个方面与之间的容器有明显的区别：

- 不支持随机存取
- 任意位置插入删除都很快
- 插入删除元素不会导致其他元素的指针、引用、迭代器失效

有这些区别的主要原因也是使用了链表存储的缘故，上面的基本上是链表的特性。

## List的操作函数


> 构造函数和析构函数

![](http://i.imgur.com/oE2BZ1x.png)

> 非变动性操作

![](http://i.imgur.com/fMIhisy.png)

> 赋值

![](http://i.imgur.com/0eAo0QF.png)

> 元素存取

![](http://i.imgur.com/rk5RTAD.png)

> 迭代器

![](http://i.imgur.com/NvhztQl.png)

> 插入删除

![](http://i.imgur.com/iYpawqr.png)

> 特殊操作

![](http://i.imgur.com/oJd5kFu.png)