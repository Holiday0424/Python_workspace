#多线程模式

#导入模块
import threading,time
#定义两个函数
def fir_task():
    temp_num = 0
    while temp_num < 10:
        print("这是任务1的输出")

def second_task():
    temp_num = 0
    while temp_num < 3:
        print("这是任务2的输出")
        time.sleep(1)
        temp_num += 1
