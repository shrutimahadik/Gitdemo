import pytest


@pytest.mark.usefixtures("dataLoad")
class Testexample:

    def test_editprofile(self,dataLoad): #if you pass something it is mandatory to pass fixture name into method -interview question

        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])





