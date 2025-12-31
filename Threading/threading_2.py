import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        """重写run方法"""
        print(f'自定义线程{self.num}开始执行')
        time.sleep(1)
        print(f'自定义线程{self.num}执行结束')


# 使用自定义线程类
threads = []
for i in range(3):
    t = MyThread(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('自定义线程执行完毕')
