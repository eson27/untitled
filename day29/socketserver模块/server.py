# import time
# import socket
# sk = socket.socket()
# sk.bind(('170,0.0.1',9001))
# sk.listen()
#
# conn,_=sk.accept()
# while True:
#     try:
#         content = conn.recv(1024).decode('utf-8')
#         conn.send =(content.upper().encode('utf-8')
#         time.sleep(0.5)
#     except ConnectionResetError:
#         break


import time
import socketserver

class Myserver(socketserver.BaseRequestHandler): #socketserver规定的命名，不能命名其它

    def handle(self): # 客户端服务从handle这句开始
        conn=self.request # request结果等于进行conn
        while True:
            try:

                content = conn.recv(1024).decode('utf-8')
                conn.send (content.upper().encode('utf-8'))
                print(conn)
                time.sleep(0.5)

            except ConnectionResetError:
                break
server = socketserver.ThreadingTCPServer(('127.0.0.1',9002),Myserver)
server.serve_forever()