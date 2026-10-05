# Any pytest file always start with test_ or end with _test
#In pytest method name should always start with test
# Any code should wrapp in method
#method name should have sense
#-k stands for method name execution,-s for logs in output,-v for more info metadata
#you can run specific file with py.test <filename>
#you can mark(tag)tests with @pytest.mark.smoke and then run with -m
#you can skip test with @pytest.mark.skip
#pytest.mark.xfail use to only run programm but ouput wont see in output
#fixture are used as setup and tear down methods for test cases-conftest file to generalize
#fixture and make it available to all test cases
#data driven and parameterization can be done with return format in tupples format
#when you define fixture scope to class only it will run once before class initiated and at the end


import pytest


@pytest.mark.smoke
def test_firdttest(setup):
    print("hello")

def test_secondcreditcard():
    print("good morning")


def test_crosbrowser(crossbrowser):
    print(crossbrowser)
    print(crossbrowser[0])
    print(crossbrowser[1])

