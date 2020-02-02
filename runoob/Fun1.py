#! /usr/bin/env python3
# 函数
# 必需参数
def sayName(name):
    print(name)
sayName("pjt")
# 关键字参数
def sayName1(name):
    print(name)
sayName1(name="test")
# 默认参数
def sayName2(name,age=35):
    print("名字:",name)
    print("年龄:",age)
sayName2("test2",15)

# 不定长参数 *1个星号以元组(tuple)导入
def sayName3(name,*post):
    print(name)
    print(post)
sayName3("pjt3",20,30)

# 不定长参数 **2个星号以字典导入
def sayName4(name,**post):
    print(name)
    print(post)
sayName4("pjt4",a=2,b=3,d=4)

