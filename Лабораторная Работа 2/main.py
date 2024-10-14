import inner_f
import mod_calc
import half_life
import unit_tests

def main():
  print("Внутренняя функция:\n")
  inner_f.call()
  print("\nМодифицированный калькулятор:\n")
  mod_calc.user_input()
  print("\nПолураспады изотопов:\n")
  half_life.user_input()
  print("\nunit_tests:\n")
  unit_tests.perform_unittest()


if __name__ == "__main__":
  main()
