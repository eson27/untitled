# #进程之间是隔离的
# #进程之间通信(IPC) ->Inter process communication
#     #基于文件 : 同一台机器的多个进程间
#         #使用 quque
#             #基于 socket 文件级别的通信完成数据传递
#     #基于网络 : 同一台或多台上的多进程间进程
#         #常用第三方工具:(消息中间件)
#             #memcach
#             #redis *
#             #rabbitmq
#             #kafka *
# from multiprocessing import Queue,Process
# def son(q):
#     q.put('hello') #2.-> put
# if __name__=='__main__':
#     q=Queue()  # 1.实例化 队列Queue
#     p=Process(target=son,args=(q,))
#     p.start()
#     p.join()
#     print(q.get()) # 3->get 先进先出
# #三步实现队列化(进程间通信)


'''
生产者消费者模型
    爬出的时候
    分布式操作 :celery
'''
from multiprocessing import Process,Queue
import time
def consumer(q): #消费者
    for i in range(10):
        print(q.get()) #get 没有参数
def producer(q): #生产者
    for i in range(10):
        time.sleep(1)

        q.put(i)  #put带参数
if __name__=='__main__':
    q=Queue()
    c1=Process(target=consumer,args=(q,))
    p1 = Process(target=producer, args=(q,))

    p1.start()

    p1.join() #全部生产完再消费
    c1.start()

