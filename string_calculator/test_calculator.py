from string_calculator.calculator import add


def test_sum():
    assert add("") == 0
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("4,") == ""
    assert add("1,2,3") == 6
    assert add("1,2\n3") == 6
    assert add("2,\n3") == 5





