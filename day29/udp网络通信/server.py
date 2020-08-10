import socket
sk=socket.socket(type=socket.SOCK_DGRAM)# tcp 默认 udp用type手动输入
sk.bind(('127.0.0.1',9000))#udp不用conn

while True:
    msg,addr=sk.recvfrom(1024)
    #msg=sk.recv(1024)
    smsg=input("input:")
    print(msg.decode('utf-8'),addr)
    sk.sendto(smsg.encode('utf-8'),addr)