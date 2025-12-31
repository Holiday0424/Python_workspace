import threading

#共享资源
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000000):
        lock.acquire()   #获取锁
        try:
          counter += 1
        finally:
          lock.release() #释放锁

threads = [] #创建5个线程
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'最终计数器值: {counter}')   #值应该是5000000