
class variable:
    num=100
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def summation(self):
        return self.a+self.b

obj=variable(2,3)
print(obj.summation())


obj=variable(4,5)
print(obj.summation()+variable.num)