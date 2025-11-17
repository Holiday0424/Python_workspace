def diyexception(level):
    if level > 0:
        raise Exception("raise exception", level)
        print('这里不执行')

try:
    diyexception(3)
except Exception as e:#捕捉异常
    print(e)
