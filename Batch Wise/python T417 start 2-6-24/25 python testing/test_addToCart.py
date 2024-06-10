import pytest

@pytest.fixture()
def setUp():
   print("open browser")
   print("open website")
   print("do login")
   yield
   print("do logout")
   print("close browser")

def test_addtocart(setUp):
   print("clicked on button add to cart")