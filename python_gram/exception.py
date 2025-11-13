def diyException(level):
    if level > 0:
        raise Exception("raise exception", level)
        print('这里不执行')

try:
    diyException(3)
except Exception as e:#捕捉异常
    print(e)
