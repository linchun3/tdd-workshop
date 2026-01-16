from string_calculator.calculator import add
import pytest

def test_empty_str():
    assert add("") == 0

def test_single_num():
    assert add("1") == 1

def test_double_num():
    assert add("1,2") == 3

def test_triple_num():
    assert add("1,2,3") == 6

def test_line_break():
    assert add("1,2\n3") == 6
    assert add("2,\n3") == 5

def test_special_delimiter():
    assert add("//;\n1;3") == 4
    assert add("//|\n1|2|3") == 6

def test_ends_in_delimiter():
    with pytest.raises(ValueError):
        add("4,")

def test_negative_numbers():
    with pytest.raises(ValueError):
        add("-4,1")
