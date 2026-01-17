import threading
import time
from turtledemo.sorting_animate import qsort


def worker(num):
    #线程执行函数
    print(f'线程{num}开始执行')
    time.sleep(2)  #模拟耗时操作
    print(f'线程{num}执行完毕')

#创建线程对象
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start() #启动线程

#阻塞，等待所有线程执行完毕
for t in threads:
    t.join() #等待线程结束
    print(f'线程{t.name}执行完毕')