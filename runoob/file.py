#! /usr/bin/env python3
# 文件
fo=open("D:/123.txt","r+")
print(fo.read(100))
fo.seek(0,2)
fo.write("\ryoufuck")
fo.close()
fo=open("D:/123.txt","r+")
print(fo.read(100))
fo.close()