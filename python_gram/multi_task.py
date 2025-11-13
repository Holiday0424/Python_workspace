#多线程模式

#导入模块
import threading,time
#定义两个函数
def fir_task():
    temp_num = 0
    while temp_num < 10:
        print("这是")