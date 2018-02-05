# /usr/bin/env python
# _*_ coding:utf-8 _*_
# 字符串和列表知识点

import string
import keyword
from string import Template

alphas = string.letters + '_'
nums = string.digits

print "Testees must be at least 2 chars long."
# myInput = raw_input("Please input a char:")
myInput = "Please"

# 字符串切片操作 正向索引，反向索引，默认索引
print myInput[1:3],    # 结果le
print myInput[1:]
print myInput[:4]
print myInput[-3:-1]  # :没有给出的话就默认是结束或开始位置 倒序就是从最后一个-1开始
print myInput[::-2]   # 简单的步长倒序截取
print myInput[::1]    # 分割正序分割截取
# 标识符检查：首先要以字母或下划线开始，后面要跟字母或者下划线，或者数字
# 原始字符串操作符 r/R 大小写没有区别，r必须紧靠在第一个字符引号前 通常在打开文件名和正则表达式中用到
if len(myInput) > 1:

    if myInput[0] not in alphas:
        print '''invalid: first symbol must be
            alphabetic'''
    else:
        for otherchar in myInput[1:]:

            if otherchar not in alphas + nums:
                print '''invalid: remaining
                    symbols must be alphanumeric'''
                break
        else:
            if myInput in keyword.kwlist:
                print 'It is keyword of python!'
            else:
                print "Ok as an identifier"
# for循环的else语句是一个可选项，只在for循环完整的结束，没有遇到break时执行
s = "auth112d"
print string.upper(s[:3] + s[3])
print s.upper()
print '%s %s' % ('A', 'b')
s1 = ' '.join(('ship', 'hi'))   # join 列表
print s1
s2 = 'Hello' + u' ' + 'world'   # 连接操作前转化为unicode
print s2
print 'line', '23'              # 自动连接

# 字符串模板
s3 = Template('There are ${how_many} ${lang} Quotation Symbols')
print s3.substitute(lang='Python', how_many=3)
print 'There are %(how_many)d %(lang)s Quotation Symbols' % {'how_many': 12, 'lang': 'Python'}
cmp(s, s1)
len(s)
max(s), min(s)
s.strip()                       # 移除字符串头尾的字符（默认为空格）
t = 'foo bar'
for i, j in enumerate(t):
    print i, j
s10, t10 = 'deeabt', 'seedfh'
print zip(s10, t10)
str(s), unicode(s2)             # 产生所对应类型的对象
chr(255)                        # 以0-255做参数，返回一个字符
unichr(2)                       # 返回unicode字符 参数范围依赖于Python是如何被编译的
ord('c')                        # 以一个长度为1的字符串作为参数，返回对应的ASCII数值，或者Unicode值
print t.split("o", 1)

# 序列类型函数
aList = [12, 2]
seq = [1, 2]
sorted(aList), reversed(aList), len(aList), max(aList),\
    min(aList), sum(aList), enumerate(aList), zip(aList, seq), tuple(aList)
anotherList = list(tuple(aList))
# aList == anotherList # result is true
# aList is anotherList # result is false
# ==是因为是相同的数据集合， not is 是因为变量指向的不是同一个对象了

# 列表类型的内建函数
aList.append('a11')
aList.count(12)     # 计算列表中单个元素的个数
aList.extend(seq)
# print aList.extend(seq) 结果返回None，是因为extend是原地操作，所以打印到屏幕上的是extend()方法的结果 None,
# 还是会改变list
# aList.pop(0)         # 删除指定index位置的值，默认是index=-1，但是index不能超出范围
aList.remove('a11')      # 删除列表中的元素
aList.reverse()      # 原地反转列表
aList.sort()         # 以指定的方式排序列表中的成员，
print aList
# 列表解析
a = [i for i in range(6)]
b = ['sm' + j for j in range(8) if j % 2 == 0]
print('\n'.join([''.join(['%s*%s=%-2s'% (x,y,x*y) for x in range(1,y+1)]) for y in range(1, 10)]))
