import unittest
import mod_calc

class TestCalc(unittest.TestCase):
  def test_calc_add(self):
    result = mod_calc.calc("+",8,2)
    self.assertEqual(result, 10)
  def test_calc_sub(self):
    result = mod_calc.calc("-",8,2)
    self.assertEqual(result, 6)
  def test_calc_mul(self):
    result = mod_calc.calc("*",8,2)
    self.assertEqual(result, 16)
  def test_calc_div(self):
    result = mod_calc.calc("/",8,2)
    self.assertEqual(result, 4)
  def test_div_by_zero(self):
    result = mod_calc.calc("/",100,0)
    self.assertEqual(result, "Деление на ноль")

def perform_unittest():
  unittest.main(module = "unit_tests")