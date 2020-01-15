#!/usr/bin/python3
import pymysql
db=pymysql.connect("192.168.192.118","root","pan19881220.","ISeeTest")
cursor=db.cursor()
cursor.execute("select * from User")
data=cursor.fetchall()
for i in data:
    print(i)
    