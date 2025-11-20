# r:只读模式
f = open('python_test.txt', 'r', encoding='utf-8')
#1 全读取，内存容易溢出
#print(f.read())

#2 只读一行
#print(f.readline())

#3 for循环（重点）
# for line in f:
#     print(line.strip()) #去掉换行

#4 前面一行单独读取，后面的数据用for循环
# first_line = f.readline()
# for line in f:
#     print(line.strip())

#W 只写模式，重新创建文件
# f = open("b.txt", mode="w", encoding="utf-8")
# f.write("周杰伦")
# f.write("\n")  # 换行
# f.write("哈哈")

# # a: append 追加写. 不会重新创建文件, 但是如果文件不存在, 可以创建文件
# f = open("c.txt", mode="a", encoding="utf-8")
# f.write("你好")