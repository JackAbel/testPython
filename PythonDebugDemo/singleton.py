#! /usr/env/python


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(Singleton):
    a = 1


class Singleton2(object):
    _dict = {}

    def __new__(cls, *args, **kwargs):
        ds = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        ds.__dict__ = cls._dict
        return ds

fn = lambda n: n if n <= 2 else fn(n-1) + fn(n-2)