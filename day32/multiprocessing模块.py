#multiprocessing 多元的处理进程模块
# from multiprocessing import Process #
# import os
# def func():
#     print(os.getpid(),os.getppid())
# print('123') # 在windows 执行两次 mac只一次
# if __name__=='__main__':    # 说明父、子进程关系
#     #只会在主进程中执行所有代码
#     print('main:',os.getpid(),os.getppid()) # 父id->os.getpid(), 子id->os.getppid()
#     p=Process(target=func)
#     p.start()  #开启一个子进程

from multiprocessing import Process #
import os
def func(name,age):
    print(os.getpid(),os.getppid(),name,age)
print('123') # 在windows 执行两次 mac只一次
if __name__=='__main__':    # 说明父、子进程关系
    #只会在主进程中执行所有代码
    print('main:',os.getpid(),os.getppid()) # 父id->os.getpid(), 子id->os.getppid()
    arg_list=[['fd',20],['dfds',40],['opo',50]]
    for i in arg_list:
        p=Process(target=func,args=i)#参数 args=(元组)
        p.start()

'''
为什么要用if __name__=='__main__': 
    windows 要加 Mac 可加可不加

能不能给子进程传递参数

    可以
from multiprocessing import Process #
import os
def func(name):
    print(os.getpid(),os.getppid(),name)
print('123') # 在windows 执行两次 mac只一次
if __name__=='__main__':    # 说明父、子进程关系
    #只会在主进程中执行所有代码
    print('main:',os.getpid(),os.getppid()) # 父id->os.getpid(), 子id->os.getppid()
    p=Process(target=func,args=('alex',))#参数 args=(元组)
    p.start()  #开启一个子进程

能不能给子进程返回值
    不可以,不同内存空间

能不能同时开启多个子进程
    可以,
    
from multiprocessing import Process #
import os
def func(name,age):
    print(os.getpid(),os.getppid(),name,age)
print('123') # 在windows 执行两次 mac只一次
if __name__=='__main__':    # 说明父、子进程关系
    #只会在主进程中执行所有代码
    print('main:',os.getpid(),os.getppid()) # 父id->os.getpid(), 子id->os.getppid()
    p=Process(target=func,args=('alex',20))#参数 args=(元组)
    p.start()  #开启一个子进程1, start()异步非阻塞,不等待

    p = Process(target=func, args=('eww',30))  # 参数 args=(元组)
    p.start()  # 开启一个子进程2

    p = Process(target=func, args=('ggdx',40))  # 参数 args=(元组)
    p.start()  # 开启一个子进程3
    
    可以用for 循环
from multiprocessing import Process #
import os
def func(name,age):
    print(os.getpid(),os.getppid(),name,age)
print('123') # 在windows 执行两次 mac只一次
if __name__=='__main__':    # 说明父、子进程关系
    #只会在主进程中执行所有代码
    print('main:',os.getpid(),os.getppid()) # 父id->os.getpid(), 子id->os.getppid()
    arg_list=[['fd',20],['dfds',40],['opo',50]]
    for i in arg_list:
        p=Process(target=func,args=i)#参数 args=(元组)
        p.start()
    
    
join的用法 ->子进程加同步阻塞

from multiprocessing import Process #
import os
def func(name,age):
    print(os.getpid(),os.getppid(),name,age)
print('123') # 在windows 执行两次 mac只一次
if __name__=='__main__':    # 说明父、子进程关系
    #只会在主进程中执行所有代码
    print('main:',os.getpid(),os.getppid()) # 父id->os.getpid(), 子id->os.getppid()
    arg_list=[['fd',20],['dfds',40],['opo',50]]
    p_list=[]
    for i in arg_list:
        p=Process(target=func,args=i)#参数 args=(元组)
        p.start()
        p_list.append(p)
    for p in p_list:#在最后加阻塞在所有任务结束
        p.join()
    print('所有任务已执行完')
        
    
    
    

同步阻塞 异步非阻塞
    同步阻塞  join()
    异步非阻塞 start()
    
练习 使用一个多进程 写一个socketserver



'''