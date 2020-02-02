#! /usr/bin/env python3
# 流程控制
i = 0
while i == 0:
    age = int(input("请输入年龄:"))
    print("")
    if age <= 0:
        print("你是在逗我吧")
    elif 1 <= age <= 12:
        print("少儿时期")
    elif age > 12 and age <= 24:
        print("青年时期")
    elif 24 < age <= 35:
        print("中年人")
    else:
        print("old Man")