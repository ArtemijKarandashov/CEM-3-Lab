from unittest.mock import mock_open, patch
from calc import load_settings, write_log, calc, calculate_with_params

def test_load_settings():
    mock_file = mock_open(read_data='tolerance=0.0001\nout=output.txt\n')
    with patch('builtins.open', mock_file):
        expected = {
            "tolerance": "0.0001",
            "out": "output.txt",
        }
        result = load_settings("settings.ini")
        assert result == expected

def test_write_log():
    mock_file = mock_open()
    with patch('builtins.open', mock_file):
        write_log(1, 2, action='+', result=3)
        mock_file().write.assert_called_once_with('+:(1, 2) = 3\n')

def test_calc_addition():
    result = calculate_with_params(1, 2, 3, oper='+')
    assert result == 6

def test_calc_subtraction():
    result = calculate_with_params(5, 2, oper='-')
    assert result == 3

def test_calc_multiplication():
    result = calculate_with_params(2, 3, oper='*')
    assert result == 6

def test_calc_division():
    result = calculate_with_params(6, 2, oper='/')
    assert result == 3

def test_calc_division_by_zero():
    result = calculate_with_params(6, 0, oper='/')
    assert result == 0

def test_calc_mean():
    result = calculate_with_params(1, 2, 3, oper='mid')
    assert result == 2

def test_calc_variance():
    result = calculate_with_params(1, 2, 3, oper='var')
    assert result == 0

def test_calc_std_dev():
    result = calculate_with_params(1, 2, 3, oper='std_dev')
    assert result == 1

def test_calc_median():
    result = calculate_with_params(1, 3, 2, oper='med')
    assert result == 2
