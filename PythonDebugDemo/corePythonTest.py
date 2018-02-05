#! /usr/bin/env python
# _*_ coding:utf-8 _*_
import string
import random
import datetime
import time
import os

"""
3-1 为什么Python中不需要变量名和变量类型的声明？
变量在第一次赋值时自动声明，在声明时，解释器会根据语法和右侧的操作数来确定变量类型
3-2 为什么Python中不需要声明函数类型？
函数没有定义数据的返回类型，python不指定返回值的数据类型，没有return时，返回None
3-3 变量名前后不使用双下划线的原因
因为系统定义的变量用__xxx__表示
3-4 python中一行可以书写多个语句吗?
可以书写多个语句，用；分开，但是一般不会这么做，影响可读性
3-5 在Python中可以将一个语句分成多行书写吗？
可以，用\连接
3-6 (a)赋值语句x,y,z = 1,2,3;执行z,x,y = y,z,x 后x,y,z分别含有什么值
因为相当于并行的单独赋值，3,1,2
4-1 简单描述下Python对象有关的三个属性
对象的身份，类型，值 身份是每个对象的id()
4-2 类型。不可更改(immutable)指的是什么？Python的那些类型是可更改的，那些不是
不可更改是值一旦创建不可更改，python中的数字，字符串，元组不可更。tuple，dict可更改
4-3 哪些Python类型是按照顺序访问的，它们和映射类型的不同是什么？
字符串，list，tuple是顺序访问的，序列类型是容器内的数据按照从索引0开始访问，映射是哈希键值对的集合
4-5 repr()与``等价，str() 与 repr()的区别
str()获得字符串可读性好，repr()可以通过eval获得原始对象，对python友好
4-6 对象相等。你认为type(a)==type(b)和type(a) is type(b)之间的不同是什么？为什么会选择后者？函数isinstance()与这有什么关系
值的比较和身份的比较，选择后者是节省比较的时间，isinstance判断对象类型可以接受一个类型元组进行判断
5-1 讲讲Python普通整型和长整型的区别
python的标准整型相当于C语言的长整型，而其长整型大小取决于机器支持的内存大小
5-2 写一个函数，计算并返回两个数的乘积，写一段代码调用这个函数，并显示它的结果 """

# 6-1
s = 'we are people'
print 'ree' in s,
# 6-3
"""string = raw_input('Please input 4 numbers:')
listNum = string.split(',')
listNum1 = map(int, listNum)
listNum1.sort(reverse=True)
listNum.sort(reverse=True)
print listNum1
"""
# 6-5-b
s = 'string'
d = 'sTring'
if len(s) != len(d):
    pass
else:
    for i in xrange(len(s)):
        if s[i] != d[i]:
            print 'no match'
            break
    else:
        print 'm'
# 6-6-c
alist = ['string ', 'char\n', 'string']


def strmatchstr(l):
    for xy in range(0, len(l)-1):
        for j in range(xy+1, len(l)):
            if l[xy] == l[j]:
                print xy, j

strmatchstr(alist)
# 6-6


def strip1(n):
    if n[0] == " ":
        n = n[1:]
    elif n[-1] == " ":
        n = n[:-1]
    else:
        return n
    return strip1(n)
print strip1('  12  ')

# 6-8


def num_to_english_num(n):

    num_28_English = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                      7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                      13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',                  18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                      50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    while n < 21:
        return num_28_English[n]
    if 20 < n < 100:
        if n % 10 == 0:
            return num_28_English[n]
        else:
            ten = n / 10
            tens = ten * 10
            digit = n % 10
            return num_28_English[tens] + '-' + num_28_English[digit]
    while 99 < n < 1000:
        if n % 100 == 0:
            return num_28_English[n / 100] + ' hundred'
        elif n % 10 == 0:
            hundreds = n / 100
            tens = n % 100
            return num_28_English[hundreds] + ' hundred and ' + num_28_English[tens]
        else:
            hundreds = n / 100
            digit = n % 10
            tens = n % 100 -digit
            return num_28_English[hundreds] + ' hundred and ' + num_28_English[tens] + '-' + num_28_English[digit]
if __name__ == '__main__':
    num_str = raw_input('Please input a number in 0~1000 ')
    try:
        num_num = int(num_str)
        print num_to_english_num(num_num)
    except TypeError, e:
        print e
# 6-10
string_lower = string.ascii_lowercase
string_upper = string.ascii_uppercase

input_string = 'Mr.Ed'
for x in range(0, len(input_string)):
    if input_string[x] in string_lower:
        input_string = input_string[0:x] + input_string[x].upper() + input_string[x+1:]
    elif input_string[x] in string_upper:
        input_string = input_string[0:x] + input_string[x].lower() + input_string[x+1:]
print input_string

# 6-11
s = '167773121'
print 'IP' + '=' + str(int(int(s) / 16777216) & 255) + '.' + str(int(int(s) / 65536) & 255) \
      + '.' + str(int(int(s) / 256) & 255) + '.' + str(int(s) & 255)
ip = '10.0.3.193'
print 'IP_num' + '=' + str(int(ip.split('.')[0]) * 16777216 + int(ip.split('.')[1]) * 65536 +
                           int(ip.split('.')[2]) * 256 + int(ip.split('.')[3]))
# 6-12


def findchr(string1, char):
    num_list = []
    for x in range(len(string1)):
        if string1[x] == char:
            num_list.append(x)
    if len(num_list) == 0:
        return -1
    else:
        return num_list


def rfindchr(string1, char):
    y = -1
    index_list = range(len(string1))[::-1]
    for x in index_list:
        if string1[x] == char:
            y = x
            break
    return y


def subchr(string1, origchar, newchar):
    index_list = range(len(string1))[::-1]
    for x in index_list:
        if string1[x] == origchar:
            string1 = string1[0:x] + newchar + string1[x+1:]
    return string1

print findchr('as1tr1ingx"', '1')
print rfindchr('asa', 'a')
print subchr('asa', 'a', 'b')
# 6-13


def atoc(co_string):
    index_x = rfindchr(co_string, '-')
    if co_string[index_x-1] == 'e' or index_x == 0:
        index_y = rfindchr(co_string, '+')
        imag_f = float(co_string[index_y:-1])
        real_f = float(co_string[:index_y])
    else:
        imag_f = float(co_string[index_x:-1])
        real_f = float(co_string[:index_x])

    return complex(real_f, imag_f)
print atoc('-1.23e-4-5j')
# 6-14


def rfindchr(string1, char):
    y = -1
    index_list = range(len(string1))[::-1]
    for x in index_list:
        if string1[x] == char:
            y = x
            break
    return y


def rochambeau(int_a, int_b):
    if int_a == int_b:
        print 'planish'
    elif int_b-int_a == 1:
        print 'b win'
    elif int_b-int_a == -1:
        print 'a win'
    elif int_b-int_a == 2:
        print 'a_win'
    else:
        print 'b win'
a = random.randint(0, 2)
b = random.randint(0, 2)
int_string = {2: 'rock', 1: 'scissor', 0: 'cloth'}
print int_string[a], int_string[b],
rochambeau(a, b)

# 6-15

a = time.mktime(time.strptime('1/03/99', "%d/%m/%y"))
b = time.mktime(time.strptime('31/01/99', "%d/%m/%y"))
print abs(a / 3600 / 24 - b / 3600 / 24)
x = '22-10-2017'
birthday = time.mktime(time.strptime(x, "%d-%m-%Y")) / 3600 / 24
now_day = time.time() / 3600 / 24
print now_day - birthday

d2 = datetime.datetime.now()
d1 = datetime.datetime.strptime('2017-10-22', '%Y-%m-%d')
print d1 - d2

# 7-1
dict1 = {'a': 1, 'b': 2}
dict2 = dict([('c', 1), ('d', 1)])
dict3 = dict1.update(dict2)

# 7-2
# 含有不可变元素的元组和frozenset可哈希的对象可做键

# 7-3
dict1 = {}.fromkeys(('a', 'cb', 'ca'), 1)
list1 = sorted(dict1.keys())
print list1
for k in list1:
    print k, dict1[k]

# 7-4
list2 = [1, 2, 3]
list3 = ['abc', 'def', 'ghi']
dict4 = dict(zip(list2, list3))

# 8-2
def foreach(f, t, i):
    while f <= t:
        print f,
        f += i
foreach(1, 9, 4)

# 8-4


def isprime(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            break

        count -= 1
    else:
        return True
    return False
print isprime(10)

# 8-5


def getfactors(number):
    halfnum = number / 2
    factors = [(x+1) for x in range(halfnum) if number % (x+1) == 0]
    print factors
getfactors(15)

# 8-9


def getf(number, n):
    number1 = number
    m = 2
    while m < n:
        sum_count = number + number1
        number1 = number
        number = sum_count
        m += 1
    return number
print getf(1, 3)

# 8-10 部分
words = 'I am chinese'
print len([x for x in words.split()])
# 8-11


def inputname():
    db = []
    c = 0
    ce = 0
    done = True
    while done:
        prompt = 'enter name %d: ' % c
        name = raw_input(prompt)
        try:
            if name == 'q':
                print 'The sorted list (by last name) is:'
                db2 = sorted(db, key=lambda d: d.split(', ')[0])
                for qname in db2:
                    print qname
                done = False
                break
            x = name.split(', ')
            if len(x) == 2 and x[0].isalpha() and x[1].isalpha():
                db.append(name)
                c += 1
            else:
                print 'Wrong format... should be Last, First.'
                ce += 1
                c += 1
                print 'you have done this %d time(s) already. Fixing input' % ce
                continue
        except (EOFError):
            print 'Wrong format... should be Last, First.'
            ce += 1
            c += 1
            print 'you have done this %d time(s) already. Fixing input' % ce
            continue
inputname()

# 8-12

# 9-6
f = open('E:\\fox.txt', 'a+')
f1 = open('E:\\test.txt', 'r')
count = -1
for d in f:
    for e in f1:
        dlist = d.split(' ')
        elist = e.split(' ')
        count += 1
        for x in range(len(dlist if len(dlist) > len(elist) else len(elist))):
            if dlist[x] != elist[x]:
                print count, x, dlist[x], elist[x]
                break
f.close()
f1.close()
# 9-7
option = {}
f2 = open(r'C://Windows//win,ini')
for line in f2:
    if line.startswith(';'):
        continue
    if line.startswith('['):
        item = []
        name = line[1:rfindchr(']')]
        option.setdefault(name, item)
        continue
    if '=' in line:
        option[name].append(line.strip())
print option
# 9-8


def module_property(m_name):
    name1 = __import__(m_name)
    m1 = dir(name1)
    for x in m1:
        print x,
        print type(getattr(name1, x)),
        print getattr(name1, x)

module_property('os')

# 9-9
module_doc = {}
module_no_doc = []
path = r'C:\Python27\Lib'
dir_list = [f[:-3] for f in os.listdir(path) if f.endswith('.py')]
for x in dir_list:
    module_doc.setdefault(x, '')
    # file_abs_name = path + os.sep + x + '.py'
    file_abs_name = ''.join([path, os.sep, x, '.py'])
    files = open(file_abs_name)
    doc = False
    for l in files:
        if l.strip().startswith('"""') and l.strip().endswith('"""') and l != '"""':
            module_doc[x] += l
            files.close()
            break
        elif l.strip().startswith('"""') or l.strip().startswith('r"""') and l > 3:
            doc = True
            module_doc[x] += l
            continue
        elif doc:
            if l == '"""':
                module_doc[x] += l
                files.close()
                break
            else:
                module_doc[x] += l
        else:
            continue
    else:
        module_no_doc.append(x)
        files.close()

print module_no_doc
print module_doc


# 9-14
f = open('E:\\fox.txt', 'r+')
print f.truncate()
f.close()
# 9-15
fn1 = open(r'E:\test.txt')
fn2 = open('E:\\fox.txt', 'a')
for x in fn1:
    fn2.write(x)
fn1.close()
fn2.close()
# 9-16  有错误，待调试

f = open('E:\\fox.txt', 'a+')

while f.tell() != 120:
    x = f.readline()
    if len(x) <= 80:
        continue
    else:
        punc = string.punctuation + ' '
        letters = string.letters
        y = -1
        if x[81] != ' ':
            y = x[:81].rfind(' ')
        else:
            y = 80
        ql = '\n' + x[y+1:].strip() + ' '
        f.seek(y - len(x), 1)
        f.truncate(len(x) - y)
        f.write(ql)
        f.seek(-(len(ql)+2), 1)

f.close()