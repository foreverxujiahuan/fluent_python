# 第三章:字典与集合
1.  标准库里所有的映射类型都是利用dict来实现的，因此他们有个共同的限制，即只有可散列的数据类型才能用做这些映射里的键
2.  可散列的数据类型应是不可变的
3.  字典中使用get可以给找不到的键指定一个默认值
4.  可以使用d.update(dict)来进行字典合并
5.  可以使用d.pop(key)来进行键值删除
6.  字典在键值不存在的时候会调用__missing__方法
7.  types库中的MappingProxyType可以实现不可修改的dict
8.  "集"这个概念在Python中算是比较年轻的，同时它的使用率也比较低。
9.  集合的本质是许多唯一对象的聚集。因此，集合可以用于去重
10. 所有的Python程序员都从经验中得出一个结论，认为字典和集合的速度是非常快的。

## 字典总结
1.  键必须是可散列的
2.  字典在内存上的开销巨大
3.  键查询很快
4.  键的次序取决于添加顺序
5.  往字典里添加新键可能会改变已有键的顺序

## 集合总结
1.  集合里的元素必须是可散列的
2.  集合很消耗内存
3.  可以很高效的判断元素是否存在于某个集合
4.  元素的次序取决于被添加到集合里的次序
5.  往集合里添加元素，可能会改变集合里已有元素的次序