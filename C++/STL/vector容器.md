# vector容器
使用vector之前要导入头文件

    #include<vector>

其中vector是一个定义于namespace std内的模板（template）：

    namespace std{
    	template <class T, class Allocator = allocator<T> >
    	class vector;
    }

> vector中的元素可以使任意类型，但是必须能够赋值和拷贝。第二个参数可有可无，是用来定义内存模型（memory model），缺省的内存模型是C++标准库提供的allocator。

## vector的特点


> vector中的元素总是存在某种顺序，支持随机存取，在末端删除或添加元素时，性能很好，但是如果在其他地方添加删除元素性能下降很多，因为每次操作后后面的每个元素都要移动，每次移动都要调用赋值操作。

### 大小(size)和容量(capacity)
> 大小就是容器实际存储的元素数量，容量是可以存储的元素数量。

> vector操作大小的函数有size()，empty()，max_size()。还有capacity()，它返回容器实际能够容纳的元素数量。



> 确定vector的容量很重要：
> 
- 一旦内存重新配置，和vector元素有关的引用，指针，迭代器都会失效
- 内存重新配置很耗时间

> 可以使用reserve()保留适当空间，避免不断重新配置内存。

> 另一种方法是在初始化时就保证足够的空间。

> 如果reserve()给的参数比实际容量还小，不会发生任何反应。

> 删除元素的时候，肯定不会超过容量，所以肯定不会引起内存重新配置，但是插入元素的时候有可能。

vector的容量不会减少，不过有个间接减少容量的方法，就是通过swap()，交换内容后，容器的容量也会交换。

    std::vector<T> (v).swap(v);
通过构造一个和原来一样的vector，但是新的容器没有预留空间，通过swap()就可以缩减容量，前提是原来的vector有多余的预留空间。

## vector的操作函数
> 构造函数和析构函数

![](http://i.imgur.com/s7L5391.png)

> 非变动性操作

![](http://i.imgur.com/NYEosKf.png)

> 赋值

![](http://i.imgur.com/LfwR7S4.png)

> 元素存取（只有at会检查越界并抛出异常，其他函数都不做检查，如果越界，会引发未定义行为）

![](http://i.imgur.com/N6iiEr5.png)

> 迭代器

![](http://i.imgur.com/HIgLJGY.png)

> 插入和删除元素（插入删除元素都会使插入删除点后面的元素的指针、引用、迭代器失效，如果引发内存重新配置，所有元素的都会失效）

> 按照下面要求这么做会比较快（性能好）


> - 在尾部插入或删除
> - 容量足够大
> - 插入或删除多个元素时，操作次数越少越好（函数调用越少越快）

![](http://i.imgur.com/4vxpreT.png)