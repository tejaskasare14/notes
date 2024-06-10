import calculator
import pytest

@pytest.mark.imp
def test_add():
   output=calculator.add(10,2)
   assert output==12
   
def test_div():
   output=calculator.div(10,2)
   assert output==5.0
   
def test_login():
   print("login success")

def test_logout():
   print("logout success")