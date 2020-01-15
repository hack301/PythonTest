#! /usr/bin/env python3
import pymysql

db = pymysql.connect("192.168.192.118", "ISee", "rsJcAWeSeX85aWGD", "ISee")
cursor = db.cursor()
cursor.execute("select * from User")
data = cursor.fetchall()
for i in data:
    print(i)
