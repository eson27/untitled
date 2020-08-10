import time
from threading import Thread,current_thread,enumerate,active_count #多线程模块 current_thread->获取当前线程ID函数
import os

def func(i):

    print('start%s'%i,current_thread().ident)
    time.sleep(1)
    print('end%s'%i)

if __name__=='__main__':
    t1=[]
    for i in range(10):
        t=Thread(target=func,args=(i,))
        t.start()
        t1.append(t)
        #print(t.ident,os.getpid())
    print(enumerate(),active_count())
    for t in t1: t.join()

    print('所有都执行完')


#线程不可以外部termanate
#线程只有执行完才结束
#enumerate 查看活着的线程,包括主线程
'''
Thread 
    守护线程
    
线程锁 *****


线程队列 ->主要记用法

线程池 进程池 *****
'''
