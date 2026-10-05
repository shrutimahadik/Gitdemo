class Browserutil:
    def __init__(self,driver):
        self.driver = driver



    def gettitle(self):
        return self.driver.title