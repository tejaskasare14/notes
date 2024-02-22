import pytest
import calculator

@pytest.mark.imp
def test_add():
   result = calculator.add(10,2)
   assert result==12
   
def test_divide():
   result = calculator.divide(10,2)
   assert result==5