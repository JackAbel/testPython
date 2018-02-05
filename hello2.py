# -*- coding: utf-8 -*-
import functools
from types import MethodType
# 闭包
'mo kuai dai ma de di yi ge zi fu chuan wei mo kuai de wen dang zhu shi'
"""内建函数中文文档：http://python.usyiyi.cn/translate/python_278/library/functions.html"""
__author__ = 'jin_xb'


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
# 返回的函数引用了变量i,但它并非立刻执行，等到2个函数都返回时，引用的变量变成了3
f1, f2, f3 = count()
print f1()
# 返回闭包时牢记的一点是:返回函数不要引用任何循环变量，或后续会发生变化的变量，一定要引用循环变量方法
# 是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变


def count1():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
# 匿名函数，关键字lambda表示匿名函数，冒号前面的x表示函数参数,匿名函数不必担心函数名冲突，匿名函数是一个韩式对象
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 7, 8])
f1 = lambda x: x * x
# 装饰器，函数对象有一个_name_属性，可以拿到函数的名字:


print functools.__name__


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'begin call %s():' % func.__name__
        func(*args, **kw)
        print 'end call %s().' % func.__name__
    return wrapper


@log
def now(x):
    print 'www' + x
now('er')


def log2(arg):
    text = arg if isinstance(arg, str) else 'call :'

    def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
    return decorator if isinstance(arg, str) else decorator(arg)


@log2('test')
def xy():
    print 'love'
xy()

# 偏函数
int2 = functools.partial(int, base=2)
print int2('1000000')
# 引用内部模块 import Hello
# 模块提高了代码的可维护性，编写程序的时候，经常引用其他模块，包括Python内置的模块和来自第三方的模块
# 每个包下面都有一个__init__.py; sys模块有一个argv变量，用list存储了命令行的所有参数。argv的第一个参数是该.py文件的名称
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


"""有了__init__方法，创建实例必须传入与init方法匹配的参数"""
bart = Student('Bart Simpson', 59)
bart.age = 8
print bart.age, bart
# dir()函数获得一个对象的所有属性和方法 类似__xxx__的属性和方法在Python中有特殊用途
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()、hasattr()可以直接操作一个对象的状态


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x
obj = MyObject()
print hasattr(obj, 'x')
print hasattr(obj, 'y')
# 给class绑定方法


def set_score(self, score):
    self.__score = score
MyObject.set_score = MethodType(set_score, None, MyObject)
s = MyObject()
s.set_score(100)
print s.__score

# __slots__来限制该class能添加的属性
# __call__定义在类中，就可以像函数一样调用类了
# type()动态创建class


def fn(name='world'):
    print ('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print h.hello()

# 应用Metaclass


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>'(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print ('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name
        attrs['__mappings__'] = mappings
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print ('SQL; %s' % sql)
        print ('ARGS: %s' % str(args))
# assert
# python 中的 while、for循环中用else，else只在循环完成后执行，else语句会跳过else块
# from bs4 import BeautifulSoup
