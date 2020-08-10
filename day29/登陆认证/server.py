import os
import socket
import hashlib

secret_key=b'alex_sb'
sk=socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr =sk.accept()
#创建一个随机字符串
rand=os.urandom(32)
#发送一个随机字符串
conn.send(rand)

#根据发送的字符串+ secret_key 进行摘要
sha=hashlib.sha1(secret_key)
sha.update(rand)
res_client=sha.hexdigest()
#等待接收客户端的摘要结果

res=conn.recv(1024).decode('utf-8')

#做比对
if res_client == res:
    print('你是一个合法的客户端')
    #如果一致，就显示是合法的客户端
    #并可继续操作
    conn.send(b'hello')
else:
    conn.close()
    #如果不一致，应立即关闭连接


#如果一致，就显示是合法的客户端