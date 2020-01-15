#! /usr/bin/env python3
#   基本语法
import keyword
# 关键字
print(keyword.kwlist)
# 第一个注释
print("Hello,Python!")
# 多行语句
total="item_one" + \
    "item_tow" + \
    "item_three"
print(total)
# 字符串
str='Runoob'
print(str)  # 输出全部字符
print(str[0:-1])    # 输出第一个到倒数第二个字符
print(str[0])   #  输入第一个字符
print(str[2:])  # 输出第3个到后面的所有字符
print(str *2)   #   输出2次字符串
print(str +' Hello')    #   拼接字符串
print('hello\nrunoob')  #   使用反斜杠  +n换行
print(r'hello\nrunoob') #   在字符串前面添加一个 r，表示原始字符串，不会发生转义

#   等待用户输入
#   input("\n\n按下 enter 键后退出。")
x="a"
y="b"
#   换行输出
print(x)
print(y)
#   不换行输出
print('.....................')
print(x,end=" ")
print(y,end="\n")
#   import 与 from...import
#   在 python 用 import 或者 from...import 来导入相应的模块。
#   将整个模块(somemodule)导入，格式为： import somemodule
#   从某个模块中导入某个函数,格式为： from somemodule import somefunction
#   从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#   将某个模块中的全部函数导入，格式为： from somemodule import *
import sys
for i in sys.argv:
    print(i)
print('\n python路径为:',sys.path)