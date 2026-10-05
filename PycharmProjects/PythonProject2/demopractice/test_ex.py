import pytest


@pytest.mark.skip
def test_team():

    print("have fun")

@pytest.mark.xfail
def test_teamcreditcard():
    print("opening")
