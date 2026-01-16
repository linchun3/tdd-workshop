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
    assert excinfo.value.args[0] == "separators should not appear at the conclusion"

    with pytest.raises(ValueError) as excinfo:
        add("1,2\n")
    assert excinfo.value.args[0] == "separators should not appear at the conclusion"


def test_step_5_fail():
    with pytest.raises(ValueError) as excinfo:
        add("//;\n1;2?3")
    assert excinfo.value.args[0] == "invalid mixed delimiters"


def test_step_5_pass():
    assert add("//;\n1;3") == 4
    assert add("//|\n1|2|3") == 6
