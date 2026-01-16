import pytest

from string_calculator.calculator import add


def test_step_1():
    # Start writing your first test here
    assert add("") == 0
    assert add("1") == 1
    assert add("12") == 12
    assert add("1,2") == 3


def test_step_2():
    assert add("1,2,3") == 6
    assert add("1,2,3,4,5") == 15


def test_step_3():
    assert add("1,2\n3") == 6


def test_step_4():
    with pytest.raises(ValueError) as excinfo:
        add("1,2,")
    assert excinfo.value.message == "separators should not appear at the conclusion"
