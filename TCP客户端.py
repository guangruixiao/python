# -*- coding: utf-8 -*-


# 创建TCP服务器,接收到客户端字符串后，加上时间戳，返回给客户端。

from socket import *



#配置与服务器端一致的地址、端口号，及缓冲区
HOST="192.168.1.101"
PORT=21569  
BUFSIZ=1024
ADDR=(HOST,PORT)


#创建套接字并连接服务器
tcpcli=socket(AF_INET,SOCK_STREAM)
tcpcli.connect(ADDR)



while True:            
    data=raw_input(">")        #输入字符串
      
    if not data:
        break
    tcpcli.send(data)          # 发送字符串
    data=tcpcli.recv(BUFSIZ)   # 接收字符串
    if not data:
        break
    print data
    

        
        
        
        