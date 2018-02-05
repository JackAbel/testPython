#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
python 在实例化过程中调用__init__()方法，当一个类被实例化时，可以定义额外的行为，比如设定一些初始值或运行一些初步诊断
代码
类名通常由大写字母打头。数据值应该使用名词作为名字，方法使用谓词(动词加对象) 方法名中间首字母应该大写(驼峰方式)
静态变量是与它们所属的类对象绑定的，不依赖任何类实例
特殊的类属性 __name__ __doc__ __bases__(所有父类构成的元组) __dict__（类的属性） __module__（类C定义所在的模块）
 __class__(实例C对应的类)

访问类属性可以通过类名或者实例来访问，但改变类属性的值只能通过类名来更新
改变可变的类属性，用实例名不会遮蔽原来类的属性，不可变的类属性则不行
类属性更改具有持久性，

类、实例和其他对象的内建函数
issubclass(sub, sup)
isinstance(shili_obj1, lei_obj2)

"""


class myClass(object):
    def __init__(self):
        self.foo = 100
myInst = myClass()
print(hasattr(myInst, 'foo'), getattr(myInst, 'foo'))
setattr(myInst, 'bar', 'my attr')
delattr(myInst, 'bar')
round()


class AddrBookEntry(object):
    """address book entry class"""

    def __init__(self, nm, ph):     # 定义构造器
        self.name = nm
        self.phone = ph

    def updatephone(self, ph):
        self.phone = ph
john = AddrBookEntry('shen', 'huo')


class EmplAddrBookEntry(AddrBookEntry):
    def __init__(self, nm, ph, id, em):     # 每个子类最好定义它自己的构造器，不然基类的构造器就会被调用
        AddrBookEntry.__init__(self, nm, ph)  # 重写基类的构造器，基类构造器就不会被自动调用了，基类构造器
        self.empid = id                         # 就必须显示写出才会被执行
        self.email = em                         # 重写__init__不会自动调用基类的__init__ 方法

    def updateEmail(self, newem):
        AddrBookEntry.updatephone(self, 51)
        super(EmplAddrBookEntry, self).updatephone(12)
        self.email = newem
print(type(3.12).__name__)


class TestClassMethod:
    def foo(cls):
        pass
    foo = classmethod(foo)
    foo1 = staticmethod(foo)
t1 = TestClassMethod()
del t1
