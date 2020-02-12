#! /usr/bin/env python3
# 错误和异常
# try/except
try:
   res= 1/1
   raise ZeroDivisionError("yrdy");
except ZeroDivisionError as err:
    print(err)
else: # 可以不需要（没有发生任何异常的时候执行。）
    print('no error')

# try-finally语句无论是否发生异常都将执行最后的代码。
try:
    res=1/1
except ZeroDivisionError as err:
    print(err)
finally:
    print("无论是否异常都执行")

