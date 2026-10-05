import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firdttest():
    msg="hello"
    assert msg=="hi" "test fail"

@pytest.mark.xfail
def test_creditcard():
    a=2
    b=3

    assert a+2==6,"addition do not match"




@pytest.fixture()
def setup():
    print("executing first")


def fixtutrmethod(setup):
    print("will execute in fixute method")