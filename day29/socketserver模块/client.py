
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9002))

while True:

    sk.send(b'hello')
    content = sk.recv(1024).decode('utf-8')
    print(content)
#调试时pycharm 允许并行 ->在run ->edit config ->右上角允许并行解打勾
