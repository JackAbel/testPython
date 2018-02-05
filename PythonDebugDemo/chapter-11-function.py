# /usr/bin/env python
# -*- coding:utf-8 -*-
from random import randint as ri


def bar():
    return 'abc', [(4-6j), 12], 'Guido'
# 如果函数返回多个对象，Python把他们聚集成一个元组返回
# 当显式的返回None，没有显示的返回对象时，便返回一个none
from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    op = choice('+-')
    numbs = [randint(1, 10) for i in range(2)]
    numbs.sort(reverse=True)
    ans=ops[op](*numbs)
    pr = '%d, %s, %d='%(numbs[0], op, numbs[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d'%(pr, ans)
            else:
                print 'incorrect... try again.'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid input... try again'


def main():
    while True:
        doprob()
        try:
            opt = raw_input('again? [Y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break
if __name__ == '__main__':
    main()

# 函数不存在调用和定义的前后关系，两个模块使用相同的变量名字也是安全的，因为句点标识对于两个模块意味了不同的命名空间
# 在函数声明后第一个没有赋值的字串，就是我们的文档字串def foo():
def foo():
    'foo() -- properly created doc string'
foo.__doc__ = 'Oops'
print foo.__doc__
# 内嵌函数整个函数体都在外部函数的作用域，如果没有任何对内部函数的外部引用，除了函数体内，任何地方都不能对其进行调用
f = lambda x,y: cmp(x, y)
# 装饰器是在函数调用之上的修饰，这些修饰仅是当声明一个函数或者方法的时候，才会应用的额外调用
"""
@decorator(dec_opt_args)
def func2Bdecorated(func_opt_args)
    ..
修饰器可以堆叠起来
@deco2
@deco1
def func():
    pass
相当于 func = deco2(deco1(func))
带参数的装饰器
@deco2(deco_args)
@deco1
def func():
func = deco(deco_args)(deco1(func))

函数通过装饰器置入通用功能的代码来降低程序复杂度。
    引入日志
    增加计时逻辑来检测性能
    给函数加入事务的能力
函数所必需的参数必须在默认参数之前

函数接收元组和字典参数
def siu(*Tuple, **Kargs):
    pass

"""


class MyClass(object):
    @staticmethod
    def staticFoo():    # 这里省略了self(因为修饰为静态方法)，在标准的类方法中self 参数是必须的,
        pass
#       staticFoo = staticmethod(staticFoo)


def foo(**theRest):
    for each_element in theRest:
        print each_element
    print theRest
a = {'a': 1, 'b': 2}
foo(**a)
foo(x=1, y=2)   # 两种调用字典参数的方式

print [n for n in [ri(1, 99) for i in range(9)] if n % 2]
s = [ri[1, 99] for i in range(9)]
filter(lambda n: n % 2, s)
map(lambda x: x+2, s)
map(None, [1, 3, 5], [2, 4, 6])
reduce((lambda x, y: x + y), range(6))

# 偏函数
from functools import partial
baseTwo = partial(int, base=2) # 关键字参数总是出现在形参之后

is_this_global = 'xyz'


def foo():
    global is_this_global
    this_is_local = 'abc'
    is_this_globa = 'def'
    print this_is_local + is_this_global
foo()   # result is abcdef
print is_this_global    # result is def
"""
闭包将内部函数自己的代码和作用域以及外部函数的作用结合起来
闭包的词法变量不属于全局名称空间或者局部的--而属于其他的名称空间，带着流浪的作用域
闭包对于安装计算、隐藏状态和在函数对象和作用域中随意切换是很有用的。闭包在GUI或者在很多
API支持回调函数的事件驱动编程中是很有用处的
回调就是函数，闭包也是函数，但是他们能携带一些额外的作用域
"""


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]
    return incr
count = counter(5)
print count()
# 生成器是一个带yiled语句的函数 yiled语句的功能就是返回一个值给调用者并暂停执行


def simpleGen():
    yield 1
    yield '2 --> punch!'

myG = simpleGen()
myG.next()          # 调用next（）方法返回对象的连续中间值
# 生成器添加了一些新的特性send() close()


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1
count = counter(6)
count.send(9)
count.close()
# time.clock() windows上第一次调用显示的进程运行的时间，第二次调用显示的是自笫一次调用到目前的时间
