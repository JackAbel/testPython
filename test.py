#! /usr/env/python
# -*- coding:utf-8 -*-


def ge_send():
    n = 0
    while True:
        n = (yield n)
r = ge_send()
r.next()

print r.send(10)
print r.next()



