from multiprocessing import Process
import time

def son1():
    while True:
        print('in son1')
        time.sleep(1)
def son2():
    for i in range(5):
        print('in son2')
        time.sleep(1)


if __name__=='__main__':
    p1=Process(target=son1)
    p1.daemon =True #表示设置p1是一个守护进程,只管主进程代码执行完,不管子进程是否执行完
    p1.start()
    p2 = Process(target=son2) # p2 执行完主进程才关
    p2.start()
    time.sleep(3)
    #p2.join() #实现p2结束主进程才结束

#主进程会等待所有的子进程结束,是为了回收子进程资源
#守护进程实际作用已不大,业界成熟监控框架如 zabbix