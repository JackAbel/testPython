#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import copy

a = ('a2',)         # 只有一个元素的元祖里加一个逗号，以防止和其它的分组操作符混淆
print isinstance(a, (int, str))
# 元组和字符串都是不可变的，改变元祖是通过现有的元组再构造一个新元组的方式解决
# 删除一个单独的元祖中的元素是不可能的，删除整个元组 del a
b = (12, 'root')
c = a + b
print 23 in c
print c[::-1]
print str(b), a < b, a == b
# 所有多对象的，逗号分隔的，没有明确用符号定义的都默认为元祖 函数返回的多对象()
print 'a', 12, [12, 's']
"""
array      所有元素是相同类型的可变序列类型
copy       提供浅拷贝和深拷贝
operator   包含函数调用形式的序列操作符，比如operator.concat(m,n) 相当于连接操作
re         Perl风格的正则表达式查找(和匹配)
StringIO/  把长字符串作为文件来操作
cStringIO  把长字符串作为文件来操作，比如read(),seek() C版的更快，但是它不能被继承
textwrap   用作包装/填充文本的函数，也有一个类
types      包含Python支持的所有类型
collection 高性能容器数据类型
"""
# 对象赋值就是简单的对象引用,对对象的浅拷贝其实是新创建了一个类型跟原对象一样，内容是原来对象的引用
# 序列类型的浅拷贝是默认类型拷贝1，完全切片操作；2，领用工厂函数，比如list[],dict[]；3，使用copy模块的copy操作
person = ['name', ['saving', 100]]
hubby = person[:]
wife = list(person)
hubby1 = copy.copy(person)
print [id(x) for x in person, hubby, wife, hubby1]
# 深拷贝创建一个新的容器对象，包含原有对象元素(引用)全新拷贝的引用--需要copy.deepcopy()
wife1 = copy.deepcopy(person)
"""警告：一 非容器类型(比如数字，字符串和其他“原子”类型的对象，像代码、类型、xrange对象)没有拷贝
        二 如果元组变量只包含原子类型对象，对它的深拷贝将不会进行"""


