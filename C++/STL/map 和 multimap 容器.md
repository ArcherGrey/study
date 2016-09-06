# map 和 multimap
> map 和 multimap 将 key/value 作为元素，进行管理，可以根据key排序准则自动将元素排序，multimap允许重复元素。

使用之前需要导入头文件

    #include<map>

map 和 multimap 是被定义于std中的模板类：

    namespace std{
    	template <class Key, class T,class Compare = less<Key>, class Allocator = allocator<pair<const Key, T>>>
    	class map;
    
    	template <class Key, class T,class Compare = less<Key>, class Allocator = allocator<pair<const Key, T>>>
    	class multimap;
    }

第一个参数作为key，第二个参数作为value，第三个参数定义排序准则，第四个参数定义内存模型。

## 特点
> 和所有关联容器一样，也是以平衡二叉树完成的。一般情况下set,multiset,map,multimap使用相同的内部数据结构。可以把set，multiset视为特殊的map,multimap。

## 操作函数
> 构造函数和析构函数

![](http://i.imgur.com/JO3F8wH.png)

> 非变动性操作

![](http://i.imgur.com/zOnYqfI.png)

> 特殊搜寻函数

![](http://i.imgur.com/KWvXGoP.png)

> 赋值

![](http://i.imgur.com/HTLTYkK.png)

> 迭代器

![](http://i.imgur.com/ZRIRgoa.png)

> 插入删除元素

![](http://i.imgur.com/tP1wAWR.png)

## 将map视为关联数组


> 通常，关联容器不提供元素的直接存取，必须依靠迭代器，不过map提供下标操作符，支持元素的直接存取，不过下标的索引中不是元素位置而是key，也就是说索引不一定是整数类别。

## map 插入的方法
- mapA.insert(pair<T,T>(a,b)) pair是对组
- mapB.insert(map<T,T>::value_type(a,b))
- mapC[a]=b