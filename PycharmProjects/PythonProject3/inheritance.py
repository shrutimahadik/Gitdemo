#class variable use as parent class here
from variable import variable


class childclass(variable):
    def __init__(self):
        variable.__init__(self,2,3)


    def getdata(self):
        print("hello")





obj=childclass()
obj.summation()
obj.getdata()