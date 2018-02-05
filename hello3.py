# -*- coding:utf-8 -*-
'except'

import sys
import codecs


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    print '中古'
    return 10 / n


def main():
    foo('2')
main()
# 磁盘IO操作，with语句来自动帮我们调用close()方法

reload(sys)
sys.setdefaultencoding("utf-8")
try:
    f = open('C:\\Users\\rzx\\Desktop\\secret.txt', 'r')
    for eachLine in f:
        line = eachLine.strip().decode('gbk', 'utf-8')
        print line
finally:
    if f:
        f.close()
#    print f.readline()
# readline()每次读取一行内容；readlines()一次读取所有内容并按行返回list
# 默认对文件的操作都是读取ASCLL编码的文本文件。要读取二进制文件，比如图片、视频，用‘rb'模式打开文件即可
# f = open('/Users/michael/test.jpg', 'rb')
# f = open('C:\\Users\\rzx\\Desktop\\secret.txt', 'w')
try:
    import cPickle as pickle
except ImportError:
    import pickle
d = dict(name='Bob', age='20')
fws = open('C:\\Users\\rzx\\Desktop\\dump.txt', 'wb')
pickle.dump(d, fws)
fws.close()
fr = open('C:\\Users\\rzx\\Desktop\\dump.txt', 'rb')
# 反序列的时候，必须能找到对应类的定义。否则反序列化操作失败
fr.seek(0)
ds = pickle.load(fr)
print ds

fr.close()

