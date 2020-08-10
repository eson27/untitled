# #----example1 for 基本tcp通信
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# while True:
#     conn,_=sk.accept()
#     while True:
#         msg=conn.recv(1024).decode('utf-8')
#         MSG=msg.upper()
#         conn.send(MSG.encode('utf-8'))

#----example2 for 基本tcp通信 + gevent
import socket
import gevent
from gevent import monkey
monkey.patch_all()




def func(conn):
    while True:
        msg=conn.recv(1024).decode('utf-8')
        MSG=msg.upper()
        conn.send(MSG.encode('utf-8'))

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

while True:
    conn,_=sk.accept()
    gevent.spawn(func,conn)
