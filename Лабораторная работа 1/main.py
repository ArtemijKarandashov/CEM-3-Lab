import Calc
import GuessGame


def main():
  print("3.1 Калькулятор")
  Calc.user_input()
  print("3.2 Угадай число")
  GuessGame.user_input()

  print("Тесты")
  print("Калькулятор")
  Calc.tester()
  print("Угадай число")
  GuessGame.tester()

main()
