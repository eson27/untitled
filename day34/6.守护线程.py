#----exmple for 守护 子线程结束 主线程才结束
# import time
# from threading import Thread
#
# def son():
#     while True:
#         print('in son')
#         time.sleep(1)
# Thread (target=son).start()


#------exmple for
import time
from threading import Thread

def son():
    while True:
        print('in son')
        time.sleep(1)

def son2():
    #while True:
    for i in range(3):
        print('in son2 ***')
        time.sleep(1)
t=Thread (target=son)

t.daemon=True #守护线程
t.start()
Thread (target=son2).start()


'''
主线程结束 ->主进程结束 （子线程结束主线程才结束）
守护线程随着主线程的结束而结束
主线程结束后仍守护子线程 -->是的  守护进程不是
    为什么->
        其它线程结束->主线程结束->主进程结束 ->所有资源回收 ->守护线程结束



'''