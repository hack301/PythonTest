#! /usr/bin/env python3
# chdir()方法用于改变当前工作目录到指定的路径。
import os,sys
retval=os.getcwd()
print(retval)
os.chdir("D:\Code")
retval=os.getcwd()
print(retval)