import unittest
from unittest.mock import patch, mock_open

from calc import load_settings, write_log, calc, calculate_with_params

class TestCalcModule(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='tolerance=0.0001\nout=output.txt\n')
    def test_load_settings(self, mock_file):
        expected = {
            "tolerance": "0.0001",
            "out": "output.txt",
        }
        result = load_settings("settings.ini")
        self.assertEqual(result, expected)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_log(self, mock_file):
        write_log(1, 2, action='+', result=3)
        mock_file().write.assert_called_once_with('+:(1, 2) = 3\n')

    def test_calc_addition(self):
        result = calculate_with_params(1, 2, 3, oper='+')
        self.assertEqual(result, 6)

    def test_calc_subtraction(self):
        result = calculate_with_params(5, 2, oper='-')
        self.assertEqual(result, 3)

    def test_calc_multiplication(self):
        result = calculate_with_params(2, 3, oper='*')
        self.assertEqual(result, 6)

    def test_calc_division(self):
        result = calculate_with_params(6, 2, oper='/')
        self.assertEqual(result, 3)

    def test_calc_division_by_zero(self):
        result = calculate_with_params(6, 0, oper='/')
        self.assertEqual(result, 0)

    def test_calc_mean(self):
        result = calculate_with_params(1, 2, 3, oper='mid')
        self.assertEqual(result, 2)

    def test_calc_variance(self):
        result = calculate_with_params(1, 2, 3, oper='var')
        self.assertEqual(result, 0)

    def test_calc_std_dev(self):
        result = calculate_with_params(1, 2, 3, oper='std_dev')
        self.assertEqual(result, 1)

    def test_calc_median(self):
        result = calculate_with_params(1, 3, 2, oper='med')
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()