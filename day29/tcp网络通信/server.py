import socket
sk=socket.socket()
sk.bind(('127.0.0.1',9001)) #申请端口0-65535
sk.listen() #开始监听
#print('sk:',sk)
while True: # 多个客户通信
    conn,addr =sk.accept() #conn里存储的是一个客户端和我的server端的连接信息,先运行client后有信息
    #print('conn:',conn)
    #conn.send(b'hello')

    while True:

        sen_msg=input("server输入:")
        conn.send(sen_msg.encode('utf-8'))

        if sen_msg.upper()=="Q":#发送请求q退出同时自已退出
            break

        msg=conn.recv(1024).decode('utf-8')# 接收长度
        if msg.upper()=='Q':break #收到对方退出请求q退出
        print(msg)

    conn.close() # 挥手

sk.close() #归还端口

#tcp 协议