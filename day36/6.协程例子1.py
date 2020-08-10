# 安装第三方模块
# #---exampl -版本1
# import gevent
#
# def func():#带有io操作的内容写在函数里，然后提交func给gevent
#     print('start func')
#     gevent.sleep(1)
#     print('end func')
#
# g1=gevent.spawn(func)
# g2=gevent.spawn(func)
# g3=gevent.spawn(func)
# #gevent.sleep(2)
# g1.join() #阻塞 直到协程g1任务执行结束
# g2.join() #阻塞 直到协程g1任务执行结束
# g3.join() #阻塞 直到协程g1任务执行结束

# #---examp2 -版本2 .joinall简化join
# import gevent
#
# def func():#带有io操作的内容写在函数里，然后提交func给gevent
#     print('start func')
#     gevent.sleep(1)
#     print('end func')
#
# g1=gevent.spawn(func)
# g2=gevent.spawn(func)
# g3=gevent.spawn(func)
# #gevent.sleep(2)
# gevent.joinall([g1,g2,g3]) #gevent.joinall() ->阻塞 直到协程g1任务执行结束


#---examp3-版本3 .joinall简化join+monkey 最终版
import time
import gevent
from gevent import monkey


monkey.patch_all() #提高规避IO效果,查看是否生效可以在倒入前后
def func():#带有io操作的内容写在函数里，然后提交func给gevent,用在requests.get,conn.recv等
    print('start func')
    #gevent.sleep(1)
    time.sleep(1)
    print('end func')

g1=gevent.spawn(func)
g2=gevent.spawn(func)
g3=gevent.spawn(func)
#gevent.sleep(2)
gevent.joinall([g1,g2,g3]) #gevent.joinall() ->阻塞 直到协程g1任务执行结束


# #---examp4-查看协程是否能生效
#
# import socket
# print(socket.socket)
# from gevent import monkey
#
# monkey.patch_all() #提高规避IO效果,查看是否生效可以在倒入前后是否一样，不一样才是有效
# print(socket.socket)