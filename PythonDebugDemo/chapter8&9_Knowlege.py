#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import argv

# 悬挂else；while for break 跳过 else；迭代iter过程中修改序列造成程序bug
# 列表解析  支持多重嵌套for循环和多个if子句
ping = [x ** 2 for x in range(6)]
pingf = map(lambda y: y ** 2, range(6))
ping1 = [x ** 2 for x in range(6) if x > 0]
juzheng = [(m+1, n+1) for m in range(3) for n in range(5)]

# 生成器是特定的函数，允许你返回一个值，然后暂停‘代码’的执行，稍后恢复
data = open('hxh.txt', 'r')
sum(len(word) for line in data for word in line.split())
rows = [1, 2, 3, 4]


def cols():
    yield 56
    yield 2
    yield 1

x_product_pairs = ((i, j) for i in rows for j in cols())

""" 文件操作
# read() readline()读取打开文件的一行， readlines()读取所有行然后把它们作为一个字符串列表返回
# writelines()接受一个字符串列表作为参数，将它们写入文件。 for eachline in file   文件迭代
# 文件移动 seek() 可以在文件指针中移动文件指针到不同的位置，offset 代表对于某个位置的偏移量，位置默认值为0，代表
从文件开头算起，1代表从当前位置算起，2代表从文件末尾算起
调用flush方法会立即把内部缓冲区的数据写入文件，而不是被动得等待输出缓冲区被写入
读取文件很大，使用文件迭代器，每次只读取和显示一行：
"""
f = open('E:\\test.txt', 'w+')
print f.tell()
f.write('test line 1\n')
f.write('test line 2\n')
f.seek(-13, 1)
print f.tell(), f.isatty(), f.next(), f.truncate(6), f.fileno(), f.mode
# f.truncate(size=file.tell()) 截取文件到最大size字节，默认为当前文件位置f.truncate()文件位置为0时是清空文件内容
# 必须以可写的几种模式打开才可以执行
#  __import__动态加载变化的模块或类和函数
# 读取所有的命令行参数
print str(sys.argv)
print argv[0]
def input_argv(argv):       # argv 作为函数参数
    pass
# 遍历多个文件的每一行 用fileinput模块
