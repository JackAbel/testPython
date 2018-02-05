# /usr/bin/env python
# -*- coding: utf-8 -*-

# idea pydev, py2.7
# w by B.X.Jin
# time: 2017.10.18

string = 'abcdef'
# 1简单的步长为-1，常用的字符串反转方法
# 2交换前后字幕的位置
# 3使用递归的方式，每次少一个字符
# 4双端队列，使用extendleft()函数
# 5使用for循环

def reserve1(st):
    return st[::-1]


def reserve2(st):
    t = list(st)
    l = len(t)
    for i, j in zip(range(l-1, 0, -1), range(l/2)):
        t[i], t[j] = t[j], t[i]
    return "".join(t)


def reserve3(st):
    if len(st) <= 1:
        return st
    return reserve3(st[1:]) + st[0]


def reserve4(st):
    pass


def reserve5(st):
    return "".join(st[len(st)-1-i] for i in range(0, len(st)))
print(reserve1(string))
print(reserve2(string))
print(reserve3(string))
print(reserve5(string))