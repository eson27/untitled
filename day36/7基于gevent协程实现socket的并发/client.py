# #----example1 for 基本tcp通信
# import socket
# import time
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
#
# while True:
#     sk.send(b'hello')
#     msg=sk.recv(1024)
#     print(msg)
#     time.sleep(0.5)

#----example2 for 基本tcp通信 +Thread 多并发
import socket
import time
from  threading import Thread
def client(i):
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))
    while True:
        sk.send(b'hello')
        msg=sk.recv(1024)
        print(i,msg)
        time.sleep(0.5)

for i in range(500):#起500个并发
    Thread(target=client,args=(i,)).start()