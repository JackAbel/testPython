#! /usr/env/python
# -*- coding: utf-8 -*-

from functools import wraps


def use_logging(func):

    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + 'is called'
        return func(*args)
    return with_logging


@use_logging
def f(x):
    """make some math"""
    return x + x * x

print f.__name__, f.__doc__