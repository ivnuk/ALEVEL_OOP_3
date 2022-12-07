"""
order of importing

1. builtin modules
2. 3rd party modules
3. Own modules
"""
import datetime as dt
import os
import sys

from requests import request

# from lesson2.dunders import Human, COMPARE_PROP

from lesson2 import dunders as dnd


def some_func(a, b=None):
    pass


if __name__ == '__main__':
    print(dnd.COMPARE_PROP)
    a = dnd.Human("aaa", 12, 183, 'm')
    print("Hello world!", dt.datetime.now())

    a_ = 1 < 2
    some_func(a=1, b=2)
