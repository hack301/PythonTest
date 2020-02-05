#! /usr/bin/env python3
import sys
for i in sys.argv:
    print(i)
print(sys.version)
print(sys.platform)

# 引用自定义模块
import supportModule
supportModule.sayName("test")
from supportModule import sayAge
sayAge(19)
