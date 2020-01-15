#! /usr/bin/env python3
#   列表
list1=['go','python','c#','java']
list2=[1,2,3,4,5,6,7]
list3=[1,2,3,'test1','test2']
#   遍历列表
print(list3[0:])
for i in list3:
    print(i)
    i=str(i)+'test'
#   更新列表
list1[0]='goto'
print(list1[0:])
#   删除列表
del list1[0]
print(list1)