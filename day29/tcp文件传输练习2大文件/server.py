import os
import json
import socket

#接收
sk=socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()
conn,_=sk.accept()
msg=conn.recv(1024).decode('utf-8')
msg=json.loads(msg)


with open(msg['filename'],'wb') as f:
    filesize=msg['filesize']
    while filesize>0:
        content=conn.recv(1024)
        print('->',len(content))
        f.write(content)
        filesize -= len(content)#收不一定长1024
with open(msg['filename'],'rb') as f:
    for line in f:
        print(line)


conn.close()
sk.close()