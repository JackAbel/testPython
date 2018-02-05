# /usr/bin/env python
# -*- coding:utf-8 -*-
import math
"""
try:
except Exception1:

except (Exception1, Exception2), argument6:

else:
    no_exceptions_detected.suite
finally:
    always_execute_suite

BaseException
    |-KeyboardException
    |-SystemExit
    |-Exception
        |-(all other current built-in exception)
支持with
    file; decimal.Context; thread.LockType; threading.Lock; threading.RLock; threading.Condition;
    threading.Semaphore; threading.BoundedSemaphore
"""
# 上下文管理 with
# try-except 和 try-finally的一种特定的配合用法是保证共享的资源的唯一分配，并在任务结束的时候释放它
# 比如文件（数据、日志、数据库等等）、线程资源、简单同步、数据库连接 with 语句的目的在于从流程图中把try、
# except和finally 关键字和资源分配释放相关代码通通去掉。
with open('E:\\fox.txt', 'r') as f:
    pass
# 触发异常
# raise [SomeException [,args [, traceback]]]
# 断言 assert expression[, arguments]
assert 1 == 0, 'One does not equal zero silly!'
try:
    assert 1 == 0, 'One does not equal zero silly!'
except AssertionError, args:
    print '%s: %s' % (args.__class__.__name__, args)


def assert_temp(expr, args=None):
    if __debug__ and not expr:
        raise AssertionError, args

# sys.exc_info() 提供了一个三元组，exc_type 异常类；exc_value 异常类的实例；exc_tranceback 跟踪记录对象
try:
    float('abc123')
except:
    import sys
    exc_tuple = sys.exc_info()
# 10-1 2 f
# 10-4 try finally 在finally执行完后try中出现的异常会继续向上抛
# 10-5
# a SyntaxError
# 10-6


def file_open(filename):
    try:
        fi = open(filename, 'r')
    except IOError:
        return None
    return fi
# 10-8


def safe_input(str_input):
    try:
        r = raw_input(str_input)
    except (EOFError, KeyboardInterrupt):
        return None
    return r
# 10-9


def safe_sqrt(x):
    try:
        y = math.sqrt(x)
    except ValueError:
        import cmath
        z = cmath.sqrt(x)
        return z
    return y