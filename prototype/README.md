# Prototype Pattern

## 定义

> 用原型实例指定创建对象的种类，并且通过复制这些原型创建新的对象。

* note: 进行clone操作后，新对象的构造函数没有被二次执行，新对象的内容是从内存里直接拷贝的

![image](http://ata2-img.cn-hangzhou.img-pub.aliyun-inc.com/56e6c262b1510b59beba7552f07522ae.png)


## 优点

1. 性能极佳，直接拷贝比在内存里直接新建实例节省不少的资源
2. 简化对象创建，同时避免了构造函数的约束，不受构造函数的限制直接复制对象，是优点，也有隐患

## 缺点

1. 深拷贝和浅拷贝的使用需要事先考虑周到

2. 某些编程语言中，拷贝会影响到静态变量和静态函数的使用

## 应用场景

1. 对象在修改过后，需要复制多份的场景
2. 需要优化资源的情况
3. 某些重复性的复杂工作不需要多次进行。如对于一个设备的访问权限，多个对象不用各申请一遍权限，由一个设备申请后，通过原型模式将权限交给可信赖的对象，既可以提升效率，又可以节约资源
