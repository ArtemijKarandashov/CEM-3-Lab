import pytest
from main import calc, convert_precision, bubble_sort

def test_convert_precision():
    assert convert_precision(0.01) == 2
    assert convert_precision(0.001) == 3
    assert convert_precision(1) == 0
    assert convert_precision(0.12345) == 5

def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([5, 2, 8, 1]) == [1, 2, 5, 8]
    assert bubble_sort([1, 1, 1]) == [1, 1, 1]

def test_calc_add():
    assert calc(1, 2, oper="+", tolerance=0.01) == 3.0
    assert calc(1.5, 2.5, oper="+", tolerance=0.01) == 4.0

def test_calc_sub():
    assert calc(2, 1, oper="-", tolerance=0.01) == 1.0
    assert calc(2.5, 1.5, oper="-", tolerance=0.01) == 1.0

def test_calc_mul():
    assert calc(2, 3, oper="*", tolerance=0.01) == 6.0
    assert calc(2.5, 3.5, oper="*", tolerance=0.01) == 8.75

def test_calc_div():
    assert calc(4, 2, oper="/", tolerance=0.01) == 2.0
    assert calc(4.5, 2.5, oper="/", tolerance=0.01) == 1.8

def test_calc_mid():
    assert calc(1, 2, 3, oper="mid", tolerance=0.01) == 2.0
    assert calc(1.5, 2.5, 3.5, oper="mid", tolerance=0.01) == 2.5

def test_calc_var():
    assert calc(1, 2, 3, oper="D", tolerance=0.01) == 1.0
    assert calc(1.5, 2.5, 3.5, oper="D", tolerance=0.01) == 1.0

def test_calc_std_dev():
    assert calc(1, 2, 3, oper="std_dev", tolerance=0.01) == 1.0
    assert calc(1.5, 2.5, 3.5, oper="std_dev", tolerance=0.01) == 1.0

def test_calc_med():
    assert calc(1, 2, 3, oper="med", tolerance=0.01) == 2.0
    assert calc(5, 10, 15, 20, oper="med", tolerance=0.01) == 12.5

def test_calc_q3q1():
    assert calc(1, 2, 3, oper="q3q1", tolerance=0.01) == 1.0
    assert calc(1.5, 2.5, 3.5, oper="q3q1", tolerance=0.01) == 1.0

def test_calc_oper():
    assert calc(1, 2, 3, oper="adasdas", tolerance=0.01) == 0

def run():
    pytest.main()