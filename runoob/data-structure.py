#! /usr/bin/env python3
# 列表 //列表可以修改，而字符串和元组不能。
a=[66.25,333,333,1,1234.5]
print(len(a))
a.append(6.22)
del a[0:2]
#a.remove(1)
#a.reverse()
print(a.index(333))
print(a)
# 集合 //集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)

# 元组 //不可修改
t=(1,2,3,4,5,6)
print(t)
# 字典
d={'name':'pjt','age':'20'}
d['age']=21
print(d)