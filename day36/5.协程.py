'''
#并发三剑客：
    # 进程
    # 线程
        正常的开发语言 多线程可以利用多核
        cpython解释器下的多线程不能利用多核：规避了所有io操作的单线程
    # 协程
        是操作系统不可见的（可操作的最小单位）
        协程本质就是一条线程，多个任务在一条线程上来回切换，
        利用协程概念实现->来规避IO操作，就达到了我们将一条线程中的IO操作降低到最低的目的
        切换并规避io的两个模块
          ->gevent =利用了 greenlet 底层模块完成的切换 + 自动规避Io的功能
            asyncio = 利用了 yield  底层语法完成的切换 +自动规避io的功能
                历史
                    # tornado  异步的web框架 -->yield from -为了更好的实现协程 ->send -为了更好的实现协程
                        asyncio模块 基于python原生的协程概念正式的被成立
                           最后 特殊的在python中提供协程功能的关键字： aysnc  await

进程 数据隔离 数据不安全 操作系统级别 开销非常大 能利用多核
线程 数据共享 数据不安全 操作系统级别 开销小 不能利用多核
协程 数据共享 数据安全 用户级别 更小 不能利用多核 协程的所有的切换都基于用户，那么只有在用户级别能够感知到的io操作才会用协程模块切换来规避（socket，请求网页的)


#---example1 for 说明协程概念
import time
def func1():
    print('start')#短IO操作照常执行
    time.sleep(1)#长IO操作切出去，执行另一个任务
    print('end')
def func2
    print('start')
    time.sleep(1)
    print('end')
func1()
func2()
'''

#---example2 for 说明协程概念-数据安全
a=0
def func():
    global a
    a=+1

import dis
dis.dis(func) #打印底层指令







