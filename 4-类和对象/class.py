# #一、类和对象基础
# #1、类定义语法
# from logging import raiseExceptions


# class ClassName:
#     """类的文档字符串"""
#     #类属性（所有实例共享）
#     class_attribute = "共享属性"

#     #初始化方法（构造函数）
#     def __init__(self,param1,param2):
#         #实例属性（每个对象独有）
#         self.instance_attr1 = param1
#         self.instance_attr2 = param2
#     #实例方法
#     def instance_method(self):
#         return f"实例方法访问：{self.instance_attr1}"    
    
# #2、创建对象（实例化）
# obj1 = ClassName("值1","值2")
# obj2 = ClassName("另一个值1","另一个值2")

# #访问属性和方法
# print(obj1.instance_attr1) #输出：值1
# print(obj2.instance_method())  #输出：实例方法访问：值1 

# #二、核心概念详解
# #1、self参数
# #代表类的当前实例
# #在方法定义中必须作为第一个参数（约定命名为self）
# #在方法调用时不需要显示传递

# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name}在叫：汪汪！")

# my_dog = Dog("大黄")
# my_dog.bark()  #相当于 Dog.bark(my_dog)           

# #2、构造方法（__init__）
# #在创建对象时自动调用
# #用于初始化对象状态
# #可以定义默认参数
# class circle:
#     def __init__(self,radius = 1.0):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# c1 = circle()  #默认为1.0
# print(c1.area())
# c2 = circle(2.0)
# print(c2.area())

# #3、实例方法VS类方法VS静态方法
# #实例方法：需要self参数，用于访问实例属性和方法
# #类方法：需要cls参数，用于访问类属性和方法
# #静态方法：不需要self或cls参数，用于执行独立于类或实例的代码
# class Myclass:
#     def instance_method(self):
#         print(f"实例方法调用，self:{self}")

#     @classmethod
#     def class_method(cls):
#         print(f"类方法调用，cls:{cls}")

#     @staticmethod
#     def static_method():
#         print("静态方法调用，不接收任何特殊参数")

# obj = Myclass()
# obj.instance_method()  #实例方法
# Myclass.class_method()     #类方法，也可以不通过实例调用
# Myclass.static_method()  #静态方法，也可以通过实例调用，

# #三、继承与多态
# #1、基本继承：子类继承父类的属性和方法
# class Animal:
#     def __init__(self,name):
#         self.name = name 

#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name}在叫：汪汪！"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name}在叫：喵喵！"    

# animals = [Dog("大黄"),Cat("小白")]
# for animal in animals:
#     print(animal.speak())  #多态：根据对象类型调用对应的方法
#     print(animal.name)  #访问实例属性

# #2、方法重写  子类可以重新定义父类的方法，实现不同的行为
# 重写方法时，子类的方法会优先调用，而不是父类的方法
class Parent:
    def greet(self,name):
        print(f"父类方法，{name}")

class Child(Parent):
    def greet(self):
        print("子类方法（重写父类方法）")
        super().greet("Holiday")   #调用父类方法
        
c = Child()
c.greet()



