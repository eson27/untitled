import os
import json
import socket
#发送
sk=socket.socket()
sk.connect(('127.0.0.1',9001))

#文件名|文件大小
abs_path=r'C:\Users\wqlai\PycharmProjects\untitled\day29\tcp文件传输练习\tem.py'
filename=os.path.basename(abs_path)
filesize=os.path.getsize(abs_path)
dic={'filename':filename,'filesize':filesize}
str_dic=json.dumps(dic)
sk.send(str_dic.encode('utf-8'))


with open(abs_path,mode='rb') as f:

#    content=f.read()
    while filesize>0:
        content=f.read(1024)
        filesize-=len(content)#tcp协议原因收不一定长1024
        sk.send(content)

sk.close()