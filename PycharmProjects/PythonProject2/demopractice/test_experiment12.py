import pytest

msg="never"
@pytest.mark.smoke
def test_demo():
   a=2
   b=4
   assert a+4==6


def test_creditcard():
    assert msg=="ok"


