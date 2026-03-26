# 一、条件语句
# 1、基本语法结构
# if 条件1：
#    #条件1为真时执行
# elif 条件2:
#     #条件1为假且条件2为真时执行
# else:
#     #所有条件都为假时执行    #   

# 2、多条件判断示例

# source = 89
# if source >= 90:
#     print("excellent")
# elif source >=80:
#     print("nice")
# else:
#     print("good")

# 3、嵌套条件语句
# x = 10 
# y = 5 

# if x > 5:
#     if y > 3:
#         print("x>5 且 y>3")
#     else:
#         print("x>5 但 有y<=3")

# 二、循环语句：while 和while...else
# 1、while 循环基础
# count =  1 
# while count <= 5:
#     print(f"当前计数：{count}")
#     count +=1

# 2、while...else 结构
# attempts =  3
# while attempts > 0:
#     password = input("请输入密码：")
#     if password== "secret":
#         print("登录成功")
#         break
#     else:
#         attempts -= 1
#         print(f"密码错误，还可以尝试{attempts}次")
# else:
#     #循环正常结束（未通过break退出）会执行这行
#     print("用户锁定！")


# 三、循环语句：for和for...else
# 1 for循环遍历序列

# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(f"水果:"{fruit})

# 2 遍历索引与值
names =["Alice","Bob","Charlie"]
for index,name in enumerate(names,start=1):
    print(f"index:{name}")

3 for... else结构
number = [2,4,6,8]
for num in number:
    if num % 2 != 0:
        print("发现奇数，循环终止")
        break
else:
    #循环正常结束（未通过break退出）时 会执行这一行
    print("未发现奇数")

 4 遍历字典
person = {"name":"Alice","age":20,"city":"New York"}
for key,value in person.items():
    print(f"{key}:{value}")

四、循环控制关键字：break 和 continue
1 break语句
用于终止整个循环
常用于条件满足时提前退出循环
for num in range(1, 11):
    if num == 7:
        print("遇到7，终止循环")
        break
    print(num)

2 continue语句
用于跳过当前迭代，继续下一次循环
常用于过滤特定条件
for num in range(1, 11):
    if num % 2 == 0:
        continue  # 跳过偶数
    print(num)  # 只打印奇数

3 循环中的嵌套控制
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        if num == 5:
            break  # 仅跳出内层循环
        print(num)
    print("行结束")  # 仍然会执行


五、 Pass语句 占位符与空操作
1 基本用法
作为空语句占位符
用于语法上需要语句但逻辑上不需要操作的情况
def unused_function():
    pass  # 保留函数结构，暂未实现

class EmptyClass:
    pass  # 保留类结构，暂未实现

if condition:
    pass  # 条件满足时暂不执行操作

2 实际应用场景
#临时禁用代码块
for num in range(10):
    #TODO 后续实现
    pass

#占位符示例
try:
    todao()
except:
    pass  #暂时不处理异常    















