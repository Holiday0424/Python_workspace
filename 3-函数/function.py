# # # # # # 一、函数基础：定义与调用
# # # # # # 1、基本语法结构
# # # # # # def 函数名
# # # # # #   """函数文档字符串(可选)"""
# # # # # #   函数体
# # # # # #   return 返回值  #可选
# # # # # from unittest import result


# # # # # 2、简单示例
# # # # # def  greet():
# # # # #     print("Hello,Python!")

# # # # # #调用函数
# # # # # greet()    

# # # # # 3、带参数的函数
# # # # # def greet_person(name):
# # # # #      print(f"Hello,{name}!")

# # # # # greet_person("Alice")     

# # # # # 4、返回值的使用

# # # # # def add_numbers(a,b):
# # # # #     return a+b

# # # # # result = add_numbers(3,5)
# # # # # print(result)   #输出 8

# # # # # 二、参数传递机制详解
# # # # # 1、位置参数与关键字参数

# # # # # def create_user(name,age,city):
# # # # #     print(f"用户信息:{name},{age}岁，来自{city}")

# # # # # # 位置参数
# # # # # create_user("Bob",20,"New York")

# # # # # #关键字参数 (可读性更好)
# # # # # create_user(name="Alice",city="London",age=20)#

# # # # # 2、默认参数
# # # # # def power(base,exponent=2):
# # # # #     return base ** exponent

# # # # # print(power(3))   #输出 9 
# # # # # print(power(2,3)) #输出 8    

# # # # #3、可变参数（*args）
# # # # def calculate_average(*numbers):
# # # #     if not numbers:
# # # #         return 0 
# # # #     return sum(numbers) / len(numbers)  

# # # # print(calculate_average(1,2,3))       #输出 2.0  
# # # # print(calculate_average(10,20,30,40)) #输出 25.0

# # # # #4、关键字可变参数 （**kwargs）
# # # # def create_profile(**info):
# # # #     """创建用户资料字典"""
# # # #     for key,value in info.items():
# # # #         print(f"{key}:{value}")

# # # # create_profile(name="charlie",age =23,occupation="Engineer")
# # # # #name:charlie 
# # # # #age:23
# # # # #occupation:Engineer

# # # # #5、参数解包示例
# # # # def  print_coordinates(x,y,z):
# # # #     print(f"坐标:{x},{y},{z}")

# # # # coords = (10,20,30)
# # # # print_coordinates(*coords) #等价于print_coordinates(10,20,30)

# # # # person = {"name":"David","age":"35"}
# # # # def print_person(name,age):
# # # #     print(f"{name} is {age} years old")

# # # # print_person(**person)
# # # # #等价于print_person(name="David",age="35")   

# # # #三、函数作用域与生命周期
# # # 1、变量作用域规则
# # # x = 10  #全局变量

# # # def scope_demo():
# # #     y = 20  #局部变量
# # #     print(f"函数内访问全局变量x:{x}")
# # #     #print(z) #会引发NameError  z未定义

# # # scope_demo()
# # # #print(y)  #会引发NameError  y是局部变量

# # # 2、global 关键字

# # # count = 0
# # # def increment():
# # #     global count   #声明使用全局变量
# # #     count +=1

# # # increment()
# # # print(count)   #输出 1

# # # 3、nonlocal 关键字(嵌套函数中使用)
# # def outer():
# #     x = 10 
# #     def inner():
# #         nonlocal x  #声明使用外层函数的变量
# #         x += 5

# #     inner()
# #     print(x)  #输出 15   

# # outer()


# # 四、高阶函数与函数式编程
# # 1、函数作为参数传递

# # def apply_operation(x,y,operation):
# #     return operation(x,y)

# # def add(a,b):
# #     return a + b 

# # def multiply(a,b):
# #     return a * b

# # print(apply_operation(3,4,add))  #输出 7
# # print(apply_operation(3,4,multiply))  #输出12 

# # 2、函数作为返回值（闭包）

# def make_multiplier(factor):
#      """返回一个乘法函数"""
#      def multiplier(x):
#          return x * factor
#      return multiplier

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))   #输出 10 
# print(triple(5))   #输出15

# #3、lambda表达式(匿名函数)

# def square(x):
#     return x ** 2

# #等价的lambda函数
# square_lambda = lambda x: x ** 2

# print(square(4))    #输出 16
# print(square_lambda(4)) #输出16

# #常用场景：排序
# names = ["Alice","Bob","Charlie","David"]
# names_sorted = sorted(names,key=lambda name:len(name))
# print(names_sorted)

# 五、函数装饰器：增强函数功能
# 1、基本装饰器示例
from unittest import result


def my_decorator(func):
    """一个简单的装饰器，打印函数调用信息"""
    def wrapper():
        print("函数调用前...")
        func()
        print("函数调用后...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()    
#函数调用前...
#Hello!
#函数调用后...

2、带参数的装饰器
def repeat(num_times):
    """重复执行函数的装饰器"""
    def decorator_repeat(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello,{name}!")

greet("World")
#Hello,World!        
#Hello,World!    
#Hello,World!    

3、类装饰器
class TimerDecorator:
    """计算函数执行时间的类装饰器"""
    def __init__(self,func):
        self.func = func 

    def __call__(self, *args, **kwargs):
        import time 
        start_time = time.time()
        result = self.func(*args,**kwargs)
        end_time = time.time()
        print(f"{self.func.__name__}执行时间：{end_time - start_time:.4f}秒")
        return result

@TimerDecorator
def slow_function(n):
    """模拟耗时操作"""
    import time
    time.sleep(n)
    return "完成"

slow_function(2)
#slow_function  执行时间   2.0001秒
# 完成            



