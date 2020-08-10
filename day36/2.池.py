'''
有多少个任务就有多少个进程或者线程
什么是池
    要在程序开始的时候，还没有提交任务先创建几个线程或者进程
    放在一个池子里，这就是池
为什么要用池
    如果先开好进程，有任务后就可以直接使用这个池中的数据了
    并且开好的线程或者进程会一直存在池中，可以被多个任务反复利用
        减小开启、关闭、调度线程/进程的时间开销
        提高操作系统效率
'''

# #--exmple for 线程池
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(a,b):
#     print(current_thread().ident,'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(current_thread().ident,'end')
#
#
# tp=ThreadPoolExecutor(4)
# for i in range(20):
#     tp.submit(func,i ,(i+1))#submit传参数

#--exmple for 进程池 同步
# import os
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(a,b):
#     print(os.getpid(),'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(),'end')
#     return a*b # 内置return方法返回程序变成同步
#
# if __name__=='__main__':
#     tp=ProcessPoolExecutor(4)
#     for i in range(20):
#         ret=tp.submit(func,i ,(i+1))#
#         print(ret.result())

#--exmple for 进程池 异步非阻塞
# import os
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(a,b):
#     print(os.getpid(),'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(),'end')
#     return a*b # 内置return方法返回程序变成同步
#
# if __name__=='__main__':
#     tp=ProcessPoolExecutor(4)
#     future_1={}
#     for i in range(20):
#         ret=tp.submit(func,i ,(i+1))#
#         future_1[i]=ret
#     for key in future_1: #用for 循环打印这步是同步阻塞
#         print(key,future_1[key].result())


#--exmple for 进程池 异步非阻塞 .map 版本
# import os
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(a):
#     b=a+1
#     print(os.getpid(),'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(),'end')
#     return a*b # 内置return方法返回程序变成同步
#
# if __name__=='__main__':
#     tp=ProcessPoolExecutor(4)
#
#     map_1=tp.map(func,range(20))# .map 是生成器对象减小for循环，它只适合传递简单参数，
#
#     for key in map_1:
#         print(type(map_1),key)

#--exmple for 进程池 异步非阻塞  回调函数

# import os
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(a,b):
#     print(os.getpid(),'start',a,b)
#     time.sleep(random.randint(1,4))
#     print(os.getpid(),'end')
#     return a*b # 内置return方法返回程序变成同步
#
# def print_func(ret):
#     print(ret.result())
#
# if __name__=='__main__':
#     tp=ProcessPoolExecutor(4)
#     future_1={}
#     for i in range(20):
#         ret=tp.submit(func,i ,(i+1))#
#         ret.add_done_callback( print_func)
#


'''

ret 一有结果立即调用print_func，变成 异步阻塞
不用顺序接收再打（同步阻塞）
    进程池->高计算的场景，没有io（没有文件操作\没有数据库操作\没有网络操作\没有input）：
        起进程的数量：multiprocessing.cup_count()*1<起池的数量multiprocessing.cup_count*2
    线程池(一般根据IO的比例定制：multiprocessing.cup_count*5  ->4*20=80
 import multiprocessing
 print( multiprocessing.cpu_count())

'''