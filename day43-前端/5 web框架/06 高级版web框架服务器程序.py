'''
简单版web框架
1.实现效果 -- 请求-响应一个html文件
2.实现二次响应
3.多线程响应

'''

import socket

from threading import Thread


server = socket.socket()
ip_port = ('127.0.0.1',9000)
server.bind(ip_port)
server.listen()

req = {'/':'06 高级版web框架-返回页面.html',
       '/04test.css':'./04test.css',
       '/04test.js':'./04test.js',
       '/1.jpg':'./1.jpg',
       '/04web.ico':'./04web.ico' }

print(req)
#使用函数-方程单个请求动作控制
def html(conn,path):
    with open(path,'rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()
r1=html
def css(conn,path):
    with open(path,'rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()
r2=css
def js(conn,path):
    with open(path,'rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()
r3=js

def jpg(conn,path):
    with open(path,'rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()
r4=jpg


def icon(conn,path):
    with open(path,'rb') as f:
        data=f.read()
    conn.send(data)
    conn.close()
r5=icon

func_use = {'/':r1,'/04test.css':r2,'/04test.js':r3,'/1.jpg':r4,'/04web.ico':r5 }

while 1:
    conn,addr = server.accept()
    # print(server.accept(),'conn:',conn,type(conn))
    from_client_msg =conn.recv(1024)
    # print(from_client_msg.decode('utf-8'))
    # sep1 获取每次请求的路径 --请求 -\r\n 切片 --用空格 ' ' 二次切片取 取第一行第二个数
    request_str=from_client_msg.decode('utf-8')
    # request_str = from_client_msg
    # print(request_str)
    # rsl=request_str.split('\r\n') # 注：坑1-split('\r\n')有时不起作用不能分割
    request_path = request_str.replace('\r\n','$$$$').split('$$$$')[0].split(' ')[1]#

    print(type(request_path),request_path)

    # print(request_path) #返回 ： / | /04test.css |/1.jpg |/04test.js|/favicon.ico--浏览器上面导航栏页签上的图标如果不返回不会报错但一直会请求，在html文件加上<link rel="icon" href="04web.ico">就会申请对应路径图标

    conn.send(b'HTTP/1.1 200 ok\r\n\r\n') # 用chorme 输入 127.0.0.1:9001 访问，收到请求回复确认建立通信|坑2-注：字符串不能有空格
    # if request_path == '/':
    #     path = '04 升级版web框架-返回页面.html'
    # else: path ='.'+ request_path
    # print(path)
    # with open(path,'rb') as f:
    #     data=f.read()
    # conn.send(data)
    # conn.close()
    # fu=func_use[request_path]
    req_path=[request_path]
    print(req_path)

    p = Thread(target=func_use[request_path],args=(conn,req[request_path]))#开启多线程
    p.start()
    # func_use[request_path](conn,req[request_path])# 不加多线程

