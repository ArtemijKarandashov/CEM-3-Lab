"""
Модуль для задания "калькулятор"
"""

import functools
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

logger.addHandler(handler)


def log_deco(func):
    """
    Декоратор для логирования вызовов функций
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Операнд: {args[0]}, числа: {args[1]} {args[2]}")
        return func(*args, **kwargs)

    return wrapper


@log_deco
def calc(oper, num1, num2):
    """
    Выполняет арифметическую операцию
    """

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        if y != 0:
            return x / y
        else:
            return "Деление на ноль"

    result = 0
    if oper == '+':
        result = add(num1, num2)
    elif oper == '-':
        result = sub(num1, num2)
    elif oper == '*':
        result = mul(num1, num2)
    elif oper == '/':
        result = div(num1, num2)
    else:
        print("Неверная операция")
    return result


def user_input():
    """
    Вводит данные от пользователя
    """
    oper = input("Операция (+ - * /): ")

    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    print(f"Результат: {calc(oper, num1, num2)}")