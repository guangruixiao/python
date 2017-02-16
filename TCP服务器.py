# -*- coding: utf-8 -*-


# 创建TCP服务器,接收到客户端字符串后，加上时间戳，返回给客户端。

from socket import *
from time import ctime


#配置地址、端口号、缓冲区
HOST="192.168.1.101"
PORT=21569  # 随机设置，未被占用即可
BUFSIZ=1024
ADDR=(HOST,PORT)


#创建套接字并绑定，设置监听
tcpser=socket(AF_INET,SOCK_STREAM)
tcpser.bind(ADDR)
tcpser.listen(5)


while True:            #无限循环，等待连接,接收后转接连接 
    tcpcli,addr=tcpser.accept()
    while True:        #无限循环，若接收到消息，则调用send(),若无，则断开
        data=tcpcli.recv(BUFSIZ)
        if not data:
            break
        tcpcli.send("[%s],%s"%(ctime(),data))
        
        #tcpcli.close()
        
        

# 出现状况   1 用了网路查来的本地IP, 这是在广域网中的，不是本机IP     2 tcpcli.close()不应该被执行
              
        
        
      
    


