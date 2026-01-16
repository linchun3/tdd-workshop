from string_calculator.calculator import add


def test_placeholder():
    # Start writing your first test here
    assert add("") == 0
    assert add("1") == 1
    assert add("12") == 12
    assert add("1,2") == 3


def test_more_than_2():
    assert add("1,2,3") == 6

def test_flexible_separators():
    