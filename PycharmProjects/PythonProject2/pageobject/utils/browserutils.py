
class browserutils:

    def __init__(self,driver):
        self.driver=driver


    def getTile(self):
        return self.driver.title
