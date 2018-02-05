#! /usr/bin/python
# -*- coding:utf-8 -*-

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime
import re

"""
 可执行的对象声明和内建函数
callable(obj)           如果obj可调用，返回Ture， 否则返回FALSE
compile(string, file, type)     从type类型中创建代码对像，file是代码存放的地方
type 的值有三个 eval 可求值表达式[和eval()一起使用] single 单一可执行语句[和exec一起使用]
               exec 可执行语句组[和exec一起使用]
eval(obj,global=globals(),locals=locals())  对obj进行求值，obj是已编译为代码对象的表达式
exec obj                执行obj、单一的python语句或python语句的集合
input(prompt=")         等同于eval(raw_input(prompt=""))
raw_input 返回的是字符串，input 把输入作为Python对象来求值并返回表达式的结果
处理那些不想每次导入都执行的代码？ 缩进它，并放入 if __name__ == '__main__'的内部
导入模块不是执行一个外部python模块最好的方法
execfile(filename)
模块是标准库的一部分，安装在site-packages里，或者仅仅是包里的模块
第三方模块不得不深入到site-packages去找它真正定位的地方
"""

"""
正则表达式
.                                   匹配任何字符（换行符除外）
^                                   匹配字符串的开始
$                                   匹配字符串的结尾
*                                   匹配前面出现的正则表达式零次或多次
+                                   匹配前面出现的正则表达式一次或多次
?                                   匹配前面出现的正则表达式零次或一次
{N}                                 匹配前面出现的正则表达式N
{M,N}                               匹配重复出现M次到N次的正则表达式
[...]                               匹配字符组里出现的任意一个字符
[..x-y..]                           匹配从字符x到y中的任意一个字符
[^...]                              不匹配此字符集中出现的任何一个字符，包括某一范围的字符

特殊字符
\d                                  匹配任何数字，和[0-9]一样 \D与\d是反义，任何非数字
\w                                  匹配任何数字字母字符和[A-Za-z0-9_]相同，\W 反义
\s                                  匹配任何空白符，和[\n\t\r\v\f]相同，\S 反义
\b                                  匹配单词边界
\nn                                 匹配一保存的子组
\c                                  逐一匹配特殊字符c(即，取消它的特殊含义，按字面匹配)
\A(\Z)                              匹配字符串的起始（结束）
正则表达式默认是贪心匹配
非贪婪操作符“？” 这个操作符可以用在“*”、“+”或“？”的后面 要求匹配到的字符越少越好
"""

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5, 10)):
    dtint = randint(0, maxint-1)
    dtstr = ctime(dtint)
    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)

    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)

data = 'Sat Aug 09 13:59:48 2003::pcksl@hkiljs.com::1060408788-5-6'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt, data)
print m.group()

# loose match
patt1 = '^(\w{3})'  # three any digit or letter as start

domains = ('.com', '.edu', '.gov')
patt2 = '[A-Z][a-z]* [A-Z][a-z]*'
patt3 = '[A-Za-z]+, [A-Za-z]'
patt4 = r"""(\b[a-zA-z_](\w|_)+\b)"""
patt5 = '^(\d{4})[ a-zA-Z]*([a-zA-Z])$'
patt6 = r'\bwww\..*\.(com|edu|gov)$'
patt7 = r"""(\+|-)?((0|[1-9]\d*)|(0[0-7]*)|(0[xX][0-9a-fA-F]+))$"""
patt8 = r"""(\+|-)?(\d+\.\d*|\d*\.\d+)((E|e)(\+|-)?\d+)?$"""
patt9 = r"""((\+|-)?(\d+\.\d*|\d*\.\d+)((E|e)(\+|-)?\d+)?){1,2}(j|J)$"""
patt10 = r'[a-zA-Z](\w|\.|_)*@(\w|\.)+$'
patt12 = r"""([0-9]{4}-[0-9]{6}-[0-9]{5}|([0-9]{4}-){3}[0-9]{4})"""
patt11 = r"""'(\w+)'"""
data = 'Linda King'
data3 = 'Lin, s'
data5 = '3111 ssss'
data6 = 'www.baidu.com'
data7 = '-0X12'
data8 = '0.2e12'
data9 = '+4.0+.3j'
data10 = 'status@com'
data11 = "<type 'int_builtin'>"
data12 = '1111-1112-1113-1123'
compile_obj = re.compile(patt4, re.IGNORECASE)

m = re.search(patt12, data12)
print(m.group())


def identify_legal(m1):
    try:
        a = re.match(patt12, m1)
        if len(a.group()) != 0:
            print('legal')
    except AttributeError:
        print('illegal')
identify_legal(data12)

