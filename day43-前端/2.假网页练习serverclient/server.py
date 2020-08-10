'''

'''
# #---example for 最简响应演示
# import socket
#
# server = socket.socket()
# server.bind(('127.0.0.1',9001))
# server.listen()
# while 1:
#     conn,addr = server.accept()
#     from_browser_msg=conn.recv(1024).decode('utf-8')
#     print(from_browser_msg)
#     conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
#     conn.send(b'<h1> hello from server</h1>') #<h1> -标签
#     conn.close()
#
#  server.close()

#---example for 响应一个html文件
import socket

server = socket.socket()
server.bind(('127.0.0.1',9001))
server.listen()

while 1:
    conn,addr = server.accept()
    from_browser_msg=conn.recv(1024).decode('utf-8')
    print(from_browser_msg)
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open ('test.html','rb') as f:
        data = f.read()
        conn.send(data)


# server.close()




