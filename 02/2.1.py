#!/usr/bin/python3.6
# #单行注释
a=5
print(a)
print(1+5)
print(type(a))#输入变量类型
#print支持多个参数
use_name="panjiangtao"
age=30
print("姓名:",use_name,"年龄:",age)
#print(input("请输入姓名"))
#浮点型
af1=5.1251424
print(af1)
#字符串拼接
str1="Hello," "World"
print(str1)
str2="hello, "
str3="World"
print(str2+str3)
#字符串与数字拼接,不可以直接拼接，需要用到repr
str5="这本书的价格是:"
str6=98.0
#print(str5+str6) #程序会报错
#使用str()将数值转换成字符串
print(str5+str(str6))
#使用repr()将数值转换成字符串
print(str5+repr(str6))
#2.4.5字符串长度
print(len(str5))
#2.4.6原始字符串
str7='Hello World' '\\'
print(str7)