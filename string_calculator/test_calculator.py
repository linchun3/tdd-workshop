from string_calculator.calculator import add
import pytest

def test_sum():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1,2,3") == 6
    assert add("1,2\n3") == 6
    assert add("2,\n3") == 5
    assert add("//;\n1;3") == 4
    assert add("//|\n1|2|3") == 6

    with pytest.raises(ValueError):
        add("4,")