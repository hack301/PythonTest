#! /usr/bin/env python3
class MyClass:
    i = 123456

    def f(name):
        print(name)

    def __init__(self):
        i = 456789


x = MyClass()
print(x.i)
