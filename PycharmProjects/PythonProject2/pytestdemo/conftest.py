import pytest


@pytest.fixture(scope="class") #scope="class" will be run once before the class initialize and after the class all methos  executed
def setup():
    print("executing first")
    yield
    print("will execute last")


@pytest.fixture()
def dataLoad():

    print("user profile is being created")
    return["shruti","mahadik","shrutimahadik@gmail.com"]

@pytest.fixture(params=[("chrome","shruti","mahadik"),("firefox","browser"),"IE"])
def crossbrowser(request): #need to use request whenever you have a value in fixture like above
    return request.param
