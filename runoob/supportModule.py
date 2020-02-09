#! /usr/bin/env python3
# Filename:supportModule
# 输出名称
def sayName(name):
    '显示名称'
    print(name)
    return
# 输出年龄
def sayAge(age):
    print(age)
    return
if __name__  =='__main__':
    print("程序自身在运行")
else:
    print("我来自另外一个模块")