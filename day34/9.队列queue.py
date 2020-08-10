#----一般队列----
# import queue
# q=queue.Queue(4)  # fifo先进先出
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q.get())


#----后进先出队列----
# from queue import LifoQueue
# q=LifoQueue(4)  #Lifo后进先出
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q.get())

#----优先线队列----
from queue import PriorityQueue
q=PriorityQueue(4)  #Lifo后进先出
q.put((3,"a")) #参数是一个数组
q.put((2,"dff"))
q.put((1,"fdf"))
q.put((0,"3e"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())