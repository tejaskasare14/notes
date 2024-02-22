import pytest
import calculations

def test_add():
   result = calculations.add(5,6)
   assert result==11
   
def test_divide():
   result = calculations.divide(10,2)
   assert result==5