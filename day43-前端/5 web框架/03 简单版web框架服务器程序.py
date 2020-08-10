'''
简单版web框架
1.实现效果 -- 请求-响应一个html文件
2.不能实现 -- html 内的二次请求的响应 如 ：a标签 href |img标签 url |form 标签 action

'''

import socket

server = socket.socket()
ip_port =('127.0.0.1',9001)
server.bind(ip_port)
server.listen()

while 1:
    conn,addr = server.accept()
    print(server.accept(),'conn:',conn,type(conn))
    from_client_msg =conn.recv(1024)
    print(from_client_msg.decode('utf-8'))


    conn.send(b'HTTP/1.1 200 ok \r\n\r\n') # 用chorme 输入 127.0.0.1:9001 访问，收到请求回复确认建立通信

    with open('03 简单版web框架-返回页面.html','rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()