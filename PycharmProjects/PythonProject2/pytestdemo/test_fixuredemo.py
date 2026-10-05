import pytest

@pytest.mark.usefixtures("setup")
class Testexample:

  def test_fixtutrmethod1(self):
     print("will execute in fixute method1")


  def test_fixtutrmethod2(self):
     print("will execute in fixute method2")


  def test_fixtutrmethod3(self):
     print("will execute in fixute method3")


  def test_fixtutrmethod4(self):
     print("will execute in fixute method4")
