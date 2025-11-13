import os
file_path = r'E:\AA-python_workspace\python'
os.chdir(file_path)  # 切换工作目录到桌面
#f = open('python_test.txt', 'r', encoding='utf-8')
f = open('python_test.txt', 'w', encoding='utf-8')
#str = f.read(5)
num = f.write('Hello Python')
#stra = f.readlines(1)
#print(str)
print(num)
#print(stra)
f.close()