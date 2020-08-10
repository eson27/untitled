# import json
# import time
# from multiprocessing import Process
# with open('ticket.py',mode='w', encoding='utf-8') as f:
#     a={"count":1}
#     json.dump(a,f)
#
# def search(i):
#     with open('ticket.py',encoding='utf-8') as f:
#         ticket = json.load(f)
#
#         print('当前余票是%s 张 '%ticket['count'])
#
#
# def buy_ticket(i):
#     with open ('ticket.py',encoding='utf-8') as f:
#         ticket=json.load(f)
#     if ticket ['count']>0:
#         ticket ['count']-=1
#         print('%s买到票了'%i)
#
#     time.sleep(0.01)
#     with open ('ticket.py',mode='w',encoding='utf-8') as f:
#         json.dump(ticket,f)
#
# if __name__ =='__main__':
#     for i in range(10):
#        # Process(target=search,args=(i,)).start()
#         Process(target=buy_ticket, args=(i,)).start()


# #---------锁进程---------------
# from multiprocessing import Lock,Process
# def func(i,lock):
#
#     lock.acquire()#拿钥匙
#     #print('被锁起来的代码')
#     print('%s拿钥匙'%i)
#     time.sleep(1)
#     lock.release() # 还钥匙
#
#
# if __name__== '__main__':
#     lock = Lock()
#     for i in range(10):
#
#         p=Process(target=func, args=(i,lock))
#         p.start()

import json
import time
from multiprocessing import Process,Lock
# with open('ticket.py',mode='w', encoding='utf-8') as f:
#     a={"count":1}
#     json.dump(a,f)

def search(i):
    with open('ticket.py',encoding='utf-8') as f:
        ticket = json.load(f)

        print('当前余票是%s 张 '%ticket['count'])


def buy_ticket(i):

    with open ('ticket.py',encoding='utf-8') as f:
        ticket=json.load(f)
    if ticket ['count']>0:
        ticket ['count']-=1
        print('%s买到票了'%i)

    time.sleep(0.01)
    with open ('ticket.py',mode='w',encoding='utf-8') as f:
        json.dump(ticket,f)

def get_ticket(i,lock):
    search(i)
    #lock.acquire()  # 拿钥匙
    with lock: #简化,避免异常中断
        buy_ticket(i)
    #lock.release()  # 还钥匙

if __name__ =='__main__':
    for i in range(10):
        lock=Lock()
       # Process(target=search,args=(i,)).start()
        Process(target=get_ticket, args=(i,lock)).start()
