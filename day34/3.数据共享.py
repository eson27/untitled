from multiprocessing import Process,Lock,Manager # 模块Manager

def change_dic(dic,lock):
    with lock:
        dic['count']-=1




if __name__== '__main__':
    a=Manager() #进程间数据共享
    lock=Lock() # 进程加锁
    dic=a.dict({'count':100})

    p_1=[]
    for i in range(100):
        p=Process(target=change_dic,args=(dic,lock))
        p.start()
        p_1.append(p)
    for p in p_1:
        p.join()
    print(dic)