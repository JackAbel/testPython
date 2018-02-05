#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 字典的学习以及练习
# 映射类型对象里哈希值（key）和指向的对象是一对多的关系
fdict = dict((['x', 1], ['y', 2]))
print dict([['x', 1], ['y', 2]]), dict([('xy'[i - 1], i) for i in range(1, 3)]), dict(x=1, y=2)
dict9 = fdict.copy()
dduct = {}.fromkeys((('x',), 'y'), 1)
for x in dduct.keys():
    print '%s, %s' % (x, dduct[x])
dddict = {1: 12, '1': 11}
print dddict.pop('1')
# dddict.clear()
print dddict
del dddict[1]
del dddict
# hash([12])
fdict.setdefault('z', 3)
print fdict.keys(), fdict.values(), fdict.items(), fdict.get('12', 'a'), fdict.iterkeys()
# python 会从左向右检查键-值对，重复的键会成最右边的值
# 元组作为字典中有效的键，必须包含不可变参数

""" 集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键，集合对应数学里的集合有子集和超集，< == <=
>= > 交集& 合集| 差补或相对补集 - 可以用in not in 判断集合元素的存在与否，set() frozenset() 可变集合是不可哈希的
不可变集合才是能hash的"""
s = set('cheeseshop')
t = frozenset('shop')
s.add('z')
s.update('pypi')
s.remove('p')
s -= set('pypi')
