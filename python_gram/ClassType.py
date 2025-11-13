class Car(object):
    name = 'BMW'
    def __init__(self, name):
        self.name = name
    def run(self,speed):
        print(self.name,speed,'行驶')

# 访问
c = Car("宝马")
c.run("100迈")