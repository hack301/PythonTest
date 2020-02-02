#! /usr/bin/env python3
# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print(sum(10, 20))
sumTotal = lambda par1, par2: par1 * par2
print(sumTotal(1, 60))


# return 返回值
def sum1(arg1, arg2):
    total = arg1 + arg2
    print("函数内:",total)
    return total
print("函数外:", sum1(10, 20))

# 强制位置参数
def f(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
f(10,20,30,40,e=50,f=60)