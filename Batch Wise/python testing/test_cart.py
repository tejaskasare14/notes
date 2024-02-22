import pytest

@pytest.fixture
def my_fixture():
   print("open browser")
   print("login")
   print("select product")
   yield
   print("placing order")
   print("payment done")
   


def test_addtoCart(my_fixture):
   print("product added to the cart")
   

def test_logout():
   print("logged out")