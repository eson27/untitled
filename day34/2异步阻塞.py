import requests # requests  是第三方库需要先用pip安装
from multiprocessing import Process,Queue
#----异步阻塞练习->用字典链接爬取网页,把拿到的页面存在本地
url_dic={
    'baidu':'https://www.baidu.com/ ',
    'zhihu':'https://zhuanlan.zhihu.com/',
   'jianshu':'https://www.jianshu.com/ ',
    'csdn': 'https://blog.csdn.net/',
}



def producer(name,url,q):
    #print(name,url)
    ret=requests.get(url)
    #print(ret.text)
    q.put((name,ret.text))

def consumer(q):
    while True:
        tup =q.get()
        if tup is None:break
        with open ('%s.html'%tup[0],encoding='utf-8',mode='w') as f:
            f.write(tup[1])


if __name__=='__main__':
    q=Queue()
    p1=[]
    #for index,url in enumerate(url_list):
    for key in url_dic:

        p=Process(target=producer,args=(key,url_dic[key],q))
        p.start()
        p1.append(p)
    Process(target=consumer, args=(q,)).start()

    for p in p1:
        p.join()
    q.put(None)




'''
    同步阻塞
        调用函数必须等待结果\cpu没工作 input sleep recv accept connect get
    
    同步非阻塞
        调用函数必须等待结果\ cpu 工作  ->调用一个高计算的函数 strip eval('1+2+3') sum max min sorted
    
    异步阻塞
        调用函数不需要立即获取结果， 而是继续做其他的事情，在获取结果的时候不知道先获取，但是总之需要等(阻塞)
    
    异步非阻塞
        调用函数不需要立即获取结果,也不需要等 start() temiante()
        

'''