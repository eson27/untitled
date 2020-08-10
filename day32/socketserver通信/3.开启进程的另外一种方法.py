#面向对象的方法,通过继承和重写run方法完成了启动子进程
#通过重写init和调用父类的init完成了给子进程传参数

from multiprocessing import Process
import os
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
