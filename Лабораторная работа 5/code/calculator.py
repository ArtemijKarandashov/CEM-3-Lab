import math
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
        logger.info(
            f"Операнд: {kwargs['oper']}, числа: {args}, точность: {kwargs['tolerance']}"
        )
        return func(*args, **kwargs)

    return wrapper


def bubble_sort(arr):
    """
    Сортировка пузырьком
    """
    new_arr = list(arr)
    for i in range(len(new_arr) - 1):
        for j in range(len(new_arr) - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr


@log_deco
def calc(*args, **kwargs):
    """
    Выполняет арифметическую операцию
    """
    if not kwargs:
        return "Не переданы параметры"
    if not args:
        return "Недостаточное количество аргументов"

    oper = kwargs['oper']
    tolerance = convert_precision(kwargs['tolerance'])

    def add():
        res = 0
        for i in args:
            res += i
        return round(res, tolerance)

    def sub():
        res = args[0]
        for i in args[1:]:
            res -= i
        return round(res, tolerance)

    def mul():
        res = 1
        for i in args:
            res *= i
        return round(res, tolerance)

    def div():
        res = args[0]
        for i in args[1:]:
            if i != 0:
                res /= i
            else:
                return "Деление на ноль"
        return round(res, tolerance)

    def mid():
        res = 0
        for i in args:
            res += i
        return round(res / len(args), tolerance)

    def var():
        res = 0
        mid_val = mid()
        for i in args:
            res += (i - mid_val) ** 2
        return round(res / ((len(args) - 1)), tolerance)

    def std_dev():
        res = 0
        mid_val = mid()
        for i in args:
            res += (i - mid_val) ** 2
        return round(math.sqrt(res / (len(args) - 1)), tolerance)

    def med():
        res = bubble_sort(args)
        if len(res) % 2 == 0:
            res = (res[round(len(res) / 2) - 1] + res[round(len(res) / 2)]) / 2
        else:
            res = res[round((len(res) - 1) / 2)]
        return round(res, tolerance)

    def q3q1():
        middle_point = round(len(args) / 2)
        sorted_args = bubble_sort(args)
        first_half = sorted_args[:middle_point]
        second_half = sorted_args[middle_point:]
        res = (second_half[round(len(second_half) / 2)] -
               first_half[round(len(first_half) / 2)])
        return round(res, tolerance)

    # Доступные операции
    calculus_functions = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "mid": mid,
        "D": var,
        "std_dev": std_dev,
        "med": med,
        "q3q1": q3q1
    }

    result = 0

    if oper in calculus_functions.keys():
        result = calculus_functions[oper]()
    else:
        print("Неизвестная операция")
        return 0

    return round(result, tolerance)


def convert_precision(precision):
    """
    Функция конвертации точности в число знаков после запятой
    """
    precision_str = str(precision)
    decimal_places = len(precision_str.split('.')[1]) if '.' in precision_str else 0
    return decimal_places



def main():
    """
    Вводит данные от пользователя
    """
    amount_of_nums = int(input("Введите количество чисел: "))

    if not amount_of_nums > 1:
      print("Слишком мало чисел")
      return 0

    nums = []

    for i in range(amount_of_nums):
      nums.append(float(input(f"{i+1}.Введите число: ")))

    operand = input("Операция (+ - * /): ")
    prec = input("Введите точность вычислений: ")

    res = calc(*nums, oper=operand, tolerance=prec)
    print(f"Результат: {res}")


if __name__ == '__main__':
    main()
