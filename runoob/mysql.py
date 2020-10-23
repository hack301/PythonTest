#!/usr/bin/env python3
import pymysql

db = pymysql.connect("192.168.192.123", "Test01", "pan19881220.", "Test01")
cursor = db.cursor()
cursor.execute("select * from is_devicecycleparamdata3 limit 0,10")
data = cursor.fetchall()
for i in data:
    print(i)
