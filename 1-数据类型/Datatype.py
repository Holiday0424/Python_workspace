#Python中常用的有6种数据类型
"""
1、数字类型  [(整型 int)、浮点数(float)、复数(complex)、布尔(bool)]
#整数：如10/-10;
#浮点数：如13.14/-13.14
#复数：如4+3j,以j结尾表示复数
#布尔：true(1)/false(0)
2、字符串
3、列表
4、元组
5、集合
6、字典
"""

# string_type = '小金要学python'
# int_type = 10
# float_type = 10.1
# complex_type = 4+3j

# print(type(string_type))
# print(type(int_type))
# print(type(float_type))
# print(type(complex_type))

#1.1、整数类型  int
# a = 10       #十进制,
# print(a)
# print(type(a))

# a = 0b1010  #二进制
# print(a)
# print(type(a))

# #1.2、浮点数 float
# x = 3.14 
# y = 1.23e-4  #科学计数法,0.000123
# print(y)

# #1.3、复数 complex
# z = 2 + 3j   #实部2，虚部3
# print(z.real)  #实部
# print(z.imag)  #虚部

# #1.4、数字运算示例
# #基本运算
# print(10 + 5)  #加法
# print(10 - 1)  #减法
# print(10 * 2)  #乘法
# print(100 / 2) #除法
# print(10 // 3) #取整除，3
# print(10 % 3) #取模，1
# print(2 ** 3) #幂运算，2的3次方，8
# #内置数学函数
# import math
# print(math.abs(-10)) #绝对值
# print(round(3.14159, 2)) #四舍五入，保留2位小数
# print(math.sqrt(16)) #平方根
# print(math.pi) #取圆周率

# #2.1 字符串创建
# #字符串是不可变的字符序列，使用单引号、双引号或三引号
# s1 ='Holiday Jin'
# s2 ="study Python"
# s3 = '''多行
# 字符串 '''
# s4 ="""multiple 
# line"""

# #2.2字符串索引和切片
# s = 'Hello,Python'
# print(s[1]) #索引，从0开始，s[1]表示第2个字符，即'e'
# print(s[-1]) #索引，从-1开始，s[-1]表示最后一个字符，即'n'
# print(s[1:10:2]) # 切片，从1开始，到5结束，步长为2，即'el,yh'
# print(s[::2]) #切片，从0开始，所以H是必有的
 
#2.3常用字符串方法
# s = "python programming"
# print(s.upper())    #转为大写
# print(s.lower())    #转为小写
# print(s.strip())    #去除首尾空格
# print(s.split())    #拆分为列表，按照空格来拆 输出 ['python','programming']
# print("-".join(s))  #连接为字符串 输出 p-y-t-h-...
# print(s.find("pro"))  #查找字符的输出位置  7
# print(s.replace("programming","study")) #替换字符串 

#2.4 字符串格式化
#f-string (Python 3.6+)
# name = 'Holiday'
# age  = '18'
# print(f"姓名: {name} 年龄：{age}")

# #format方法
# print("{} {}".format("Python","plan"))

# # %s 转换为字符串 ；%d 整数 ；%f 浮点型 
# print("Pi is approximately %.2f" %3.1415936) #取2位小数 输出3.14


# #3.1 创建元组 
# #元组不可变，适合存储类型主键的数据
# t1 = (1,2,3)
# t2 = 1,2,3    #括号可省略
# t3 = (5,)     #单元素需要逗号
# t4 = tuple([1,2,3])  #从其他序列转换

# #3.2元组操作
# t = (10,20,30,40)
# print(t[1])      # 20 
# print(t[-1])     # 40
# print(t[1:3])    # (20,30)
# print(len(t))    # 4 
# print(30 in t)   # true 

# #元组解包
# x,y,z = (1,2,3)
# print(x,y,z)


# 4.1 创建列表
# l1 = [1,2,3]    
# l2 = list("abc") 
# l3 = []         #空列表

#4.2 列表操作
fruits = ['apple','banana','cherry']

# #访问元素
# print(fruits[1])
# print(fruits[-1])

# #修改元素
# fruits[0] = 'orange'

# #添加元素
# fruits.insert(1,'watermaleon')  #末尾添加
# fruits.append('strawberry')     #指定位置插入

#删除元素
#fruits.pop()  #删除最后一个
#fruits.remove('apple') #删除指定值

#其他操作
fruits.sort()         #排序
fruits.reverse()      #反转
print(len(fruits))









