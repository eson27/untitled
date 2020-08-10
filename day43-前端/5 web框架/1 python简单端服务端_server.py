'''
1.实现最简web框架


'''
# # 1.最简web框架 v1.0 -实现浏览器访问-回复'hello this is from server!!'
# import socket
#
# server = socket.socket()
# ip_port =('127.0.0.1',9001)
# server.bind(ip_port)
# server.listen()
#
# while 1:
#     conn,addr = server.accept()
#     print(server.accept(),'conn:',conn,type(conn))
#     from_client_msg =conn.recv(1024)
#     print(from_client_msg.decode('utf-8'))
#
#     conn.send(b'HTTP/1.1 200 ok \r\n\r\n') # 用chorme 输入 127.0.0.1:9001 访问，收到请求回复确认建立通信
#     conn.send(b'hello this is from server!!')
#
#     conn.close()

# 2.最简web框架 v1.1 -实现浏览器访问-回复html页面 --'1. html回复v1.1.html'

import socket

server = socket.socket()
ip_port =('127.0.0.1',9001)
server.bind(ip_port)
server.listen()

while 1:
    conn,addr = server.accept()
    # print(server.accept(),'conn:',conn,type(conn))
    from_client_msg =conn.recv(1024)
    print(from_client_msg.decode('utf-8'))


    conn.send(b'HTTP/1.1 200 ok \r\n\r\n') # 用chorme 输入 127.0.0.1:9001 访问，收到请求回复确认建立通信

    with open('1. html回复v1.1.html','rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()



