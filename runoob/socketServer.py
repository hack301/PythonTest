#! /usr/bin/env python3
from socket import *
from time import ctime

HOST=''
PORT=8123
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM) #创服务器套接字
tcpSerSock.bind(ADDR) #套接字与地址绑定
tcpSerSock.listen(500)  #监听连接,传入连接请求的最大数

while True:
    print('waiting for connection...')
    tcpCliSock,addr =tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data =tcpCliSock.recv(BUFSIZ).decode()
        print('date=',data)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' %(ctime(),data)).encode())

    tcpCliSock.close()
tcpSerSock.close()