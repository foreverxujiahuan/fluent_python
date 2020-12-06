# 9.符合Python风格的对象
1.  classmethod的用法是:定义操作类，而不是操作实例的方法。
2.  staticmethod装饰器也会改变方法的调用方式，但是第一个参数不是特殊的值。其实，静态方法就是普通函数，至少碰巧在类的定义中。
3.  内置的format()函数和str.format()方法把各个类型的格式化方法委托给相应的.__format__(format_spec)方法
