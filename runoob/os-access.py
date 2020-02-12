#! /usr/bin/env python3
# os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。
import os,sys
# OS操作
ret=os.access("D:/123.txt",os.F_OK) # 是否存在
print(ret)
ret=os.access("D:/123.txt",os.R_OK) # 可读
print(ret)
ret=os.access("D:/123.txt",os.W_OK) # 可写
print(ret)
ret=os.access("D:/123.txt",os.X_OK) # 可执行
print(ret)