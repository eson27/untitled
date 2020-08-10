#---exmple for 多线程数据不安全
# from threading import Thread
# n=0
# def add():
#     for i in range(200000):
#         global n
#         n+=1
# def sub():
#     for i in range(220000):
#         global n
#         n -= 1
# t1=Thread(target=add)
# t1.start()
# t2=Thread(target=sub)
# t2.start()
# t1.join()
# t2.join()
# print(n)

'''
+= -= *=  /=  while if 数据都是不安全的

列表、字典的方法操作数据都是安全的 append pop strip
lock 互斥锁
Rlock 递归锁
死锁现象 ->多把锁,互锁 解决办法把所有锁换成一把锁，用递归锁可以实现
'''

#---exmple for 多线程数据不安全->加锁
from threading import Thread,Lock
n=0
def add():
    for i in range(200000):
        global n
        with lock:
            n += 1

def sub():
    for i in range(220000):
        global n
        with lock:
            n -= 1
lock=Lock()
t1=Thread(target=add)
t1.start()
t2=Thread(target=sub)
t2.start()
t1.join()
t2.join()
print(n)
