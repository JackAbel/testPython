# -*- coding: utf-8 -*-
from collections import Iterable
print "Hello world!"


def _fact(n):
    if n == 1:
        return 1
    return n * _fact(n - 1)
print _fact(5)
# I'm good man

print isinstance('abc', Iterable)
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
for i, value in enumerate(d.values()):
    print i, value
# 列表生成式
# [x * x for x in range(1, 11)]
# [x * x for x in range(1, 11) if x % 2 == 0]
# [m + n for m in 'ABC' for n in 'XYZ']
L = ['Hello', 'World', 19, 'Apple', None]
[s.lower() for s in L if isinstance(s, str)]
# 创建Generator
g = (x * x for x in range(10))
# 高阶函数


def add(x, y, f1):
    return f1(x) + f1(y)
print add(-5, 5, abs)
# map() 函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回


def f(x, y=1):
    return x * x * y
print map(f, [1, 2, 3])
# reduce()把一个函数作用在一个序列[X1, X2, X3...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print reduce(f, [1, 2, 3])
UserName = ['adam', 'LISA', 'barT']


def fw(w):
    return w[0:1].upper() + w[1:].lower()
# print fw()
print map(fw, UserName)


def prod(y):
    def ji(a, b):
        return a * b
    for x in y:
        if isinstance(x, str):
            raise TypeError('parameter in list are not string')
#        else:
#           return reduce(ji, y) 这种方式为什么行不通！
    return reduce(ji, y)
print prod([2, 1])

# filter和map类似，也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是
# True还是False决定保留还是丢弃该元素。


def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 4, 5])
# 把一个序列中的空字符串删除


def not_empty(s1):
    return s1 and s1.strip()
filter(not_empty, ['A', '', 'B', None, 'C', ' '])
# 结果：['A', 'B', 'C']
# test 用filter()删除1～100的素数


def not_prime(n):
    def is_prime(n1):
        if n1 <= 1:
            return False
        ij = 2
        while ij * ij <= n:
            if n % ij == 0:
                return False
            ij += 1
        return True
    if is_prime(n) == False:
        return n
print filter(not_prime, range(100))
# 函数作为返回值


def lazy_sum(*args):
    def su():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return su
f = lazy_sum(1, 3, 5, 7, 9)
print f()
# print 'Hello\'s'  和 print "Hello's" 结果一致
# print 'Hello"s' and print "Hello\"s" have same result
dict1 = {}.fromkeys(('x', 'y'), -1)
