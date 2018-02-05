#! /usr/bin/python
# -*- coding: utf-8 -*-
import threading
from time import ctime, sleep


"""
GIL 全局解释器锁
在多线程环境中，python解释器运行方式如下：
1、设置GIL
2、切换到一个线程去运行
3、运行：指定数量的字节码的指令或者线程主动让出控制
4、把线程设置为睡眠状态
5、解锁GIL
模块 threading 确保重要的子线程都退出后，进程才会结束
整个python会在所有的非守护线程退出后才结束
"""
loops = [4, 2]


def action(nloop, s1):
    print('starting', nloop, 'at:', ctime())
    sleep(s1)
    print('ending', nloop, 'at:', ctime())


def main():
    threads = []
    print('starting at:', ctime())
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=action, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('All done at:', ctime())

if __name__ == '__main__':
    main()

"""
from time import sleep, ctime
import threading

loops = (4, 2)


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):                          # 创建新线程的时候，Thread对象会调用我们的ThreadFunc对象，
        self.res = self.func(*self.args)    # 这时我们已经有了要用的参数，就不用再传到Thread()构造器中


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
"""