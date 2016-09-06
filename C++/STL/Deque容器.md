# Deque容器
> 和vector非常相似，也是采用动态数组来管理元素，也提供随机存取，并有着和vector几乎一模一样的接口。不同的是deque在头尾都能快速插入删除。

在使用deque之前需要导入头文件

`#include <deque>`

deque也是定义于命名空间std内的一个类模板：

    namespace std{
    	template <class T, class Allocator = allocator<T> >
    	class deque;
    }
和vector一样，第一个参数表示元素类型，第二个参数表示内存模型。

## Deque的特点
与vector相比不同之处在于：

- 头尾都能快速插入删除元素
- 在存取元素时内部会多一个间接过程，所以速度会稍慢一些
- 迭代器需要在不同区块间跳转，所以要使用智能指针
- 不止使用一块内存，max_size()可能会更大(对内存区有限制的系统中)
- 不支持手动对容量和内存重新分配（不提供对容量操作的函数）。除头尾外，删除插入元素会使任何指向deque的指针、引用、迭代器失效。deque的内存重新分配优于vector，因为不需要复制所有元素。
- deque的内存块不再使用时会被释放，容量是可以减小的。

其他大部分接口和vector几乎一样。

## Deque操作函数
> 构造函数和析构函数

![](http://i.imgur.com/sx8In5x.png)


> 非变动性操作

![](http://i.imgur.com/D6zg9w3.png)

> 变动性操作

![](http://i.imgur.com/cCCRTYP.png)