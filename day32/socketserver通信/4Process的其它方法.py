from multiprocessing import Process
import os
import time
class Myprocess(Process):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        super().__init__()
    def run(self): #必须定义 run
        print(os.getppid(),os.getpid(),self.a,self.b,self.c)

if __name__== '__main__':
    print('-->',os.getpid())
    for i in range(10):
        p=Myprocess(1,2,3)
        p.start()
    print(p.pid,p.ident)
    print(p.name)

    p.terminate()
    print(p.is_alive())
    time.sleep(0.01)
    print(p.is_alive())