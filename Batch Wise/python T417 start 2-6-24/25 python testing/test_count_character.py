import count_character
import pytest

@pytest.mark.imp
def test_count_char():
   result = count_character.count_char("kasare","a")
   assert result==2