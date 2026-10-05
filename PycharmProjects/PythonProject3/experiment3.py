from experiement2 import glass


class example(glass):
    def one(self):
        print("one")


    def __init__(self):
     print("parent")
     super().__init__()
obj=example()
obj.one()
obj.two()