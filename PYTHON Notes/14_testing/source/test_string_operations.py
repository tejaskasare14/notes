import pytest 
import string_operations

def test_count_characters():
   name="zoozoo"
   to_count="z"
   result = string_operations.count_characters(name,to_count)
   assert result==2