#!/usr/bin/python3
import pymysql
db=pymysql.connect("106.12.82.30","root","pan19881220.","ISeeTest")
cursor=db.cursor()
cursor.execute("select * from User")
data=cursor.fetchall()
for i in data:
    print(i)