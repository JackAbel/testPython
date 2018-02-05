#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
# 11-1


def countToFour2(n=1):
    for eachNum in range(n, 5):
        print eachNum,
countToFour2(2)
# 11-2
fun = lambda x, y: x+y
print fun(1, 3)
# 11-3
# a


max2 = lambda x, y: x if cmp(x, y) else y
min2 = lambda x, y: y if cmp(x, y) else x


def my_max(*l):
    retval = l[0]
    for i in l:
        retval = max2(i, retval)
    return retval
# 11-6


def printf(a, *aTuple):
    print a % aTuple
printf('%d-%s-%s', 2016, '02', '05')
# 11-7
map(lambda x, y: (x, y), [1, 2, 3], ['a', 'b', 'c'])
zip([1, 2, 3], [4, 5, 6])
# 11-8
r_years = filter(lambda y: y % 4 == 0, [12])
r_years2 = [y for y in range(2000, 2018) if y % 4 == 0]
# 11-10
files = filter(lambda x: x and x[0] != '.', os.listdir('/root/etc/'))
# 11-11
# file size is not big
with open('E:\\fox.txt', 'r') as f:
    lines = f.readlines()
    lines2 = map(lambda x: x.strip(), lines)
    with open('E:\\Downloads\\new.txt', 'w') as f2:
        for i in lines2:
            f.write(i)
# 11-12


def timeit(func, *aTuple):
    time.clock()
    y = func(aTuple[0])
    timesum = time.clock()
    print y, timesum
# 11-13
def func(n):

    if n == 1 or n == 0:
        return 1
    else:
        return (n * func(n-1))
def func1(n):
    return reduce(lambda x, y: x * y, range(1, n))
timeit(func1, 120)
# recursion is slowly
# 11-14


def fbnq(n1, n2, n):
    if n1 == 0 and n2 == 0:
        raise ValueError
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if n == 1:
            return n3
        else:
            return fbnq(n1, n2, n-1)
print fbnq(1,1,4)
# 11-15
# 11-16 lue

# 11-17
'a' # 偏函数是固定原函数中某几个参数后形成新的函数。currying 是使用匿名单参数函数来实现多参数函数的方法
'c'# python 实现了iter() 和 next() 方法的类对象就是迭代器，生成器是特殊的迭代器，只能遍历一次，延迟操作
# 调用的时候才执行， yield语句是一次返回一个结果，在每个中间结果挂起函数的状态，以便下次调用执行

