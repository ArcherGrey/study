# Set 和 Multiset 容器
> 两种容器都会根据特定的排序准则，自动将元素排序，不同之处在于multiset允许元素重复而set不允许。

使用两种容器之间，必须先导入头文件

    #include <set>

在头文件中两种容器是被定义在命名空间std内的模板类：

    namespace std{
    	template <class T, class Compare = less<T>, class Allocator = allocator<T> >
    	class set;
    
    	template <class T, class Compare = less<T>, class Allocator = allocator<T> >
    	class multiset;
    }

## 特点
和所有标准关联式容器类似，都是以平衡二叉树完成。自动排序的主要优点在于使二叉树搜索元素时有良好的性能。其搜索算法具有对数复杂度。

但是，自动排序会造成一个重要限制：不能直接改变元素，因为会打乱原来正确的顺序。所以要改变元素值，必须先删除旧元素，再插入新元素。

## 操作函数
> 构造函数和析构函数

![](http://i.imgur.com/VneXhJN.png)

> 非变动性操作

![](http://i.imgur.com/kIqPJzS.png)

> 特殊的搜寻函数

![](http://i.imgur.com/Uz5BiIO.png)

> 赋值

![](http://i.imgur.com/ptEvQOz.png)

> 迭代器

![](http://i.imgur.com/FYOFTAL.png)

> 元素插入和删除

![](http://i.imgur.com/6F6hHIJ.png)

