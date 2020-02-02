#! /usr/bin/env python3
# 迭代器
list=[1,2,3,4,5,6,7]
it=iter(list)
print(next(it)) #打印下一个
for x in list:
    print(x,end=" ")
