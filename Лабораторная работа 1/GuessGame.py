"""
Модуль для задания "угадай число"
"""


def bin_search(arr, x):
    """
    Функция бинарного поиска
    """
    tries = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        tries += 1
        mid = (left + right) // 2
        if arr[mid] == x:
            return {"num": arr[mid], "attempts": tries}
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return {}


def slow_search(arr, x):
    """
    Функция медленного перебора
    """
    tries = 0
    res = 0
    for i in arr:
        tries += 1
        if i == x:
            res = i
            break
    return {"num": res, "attempts": tries}


def game(num, min, max):
    result = bin_search(range(min, max), num)
    print("Результаты бинарного поиска:\nВаше число: " + str(result["num"]) +
          "\nКоличество попыток: " + str(result["attempts"]))
    result = slow_search(range(min, max), num)
    print("Результаты медленного поиска:\nВаше число: " + str(result["num"]) +
          "\nКоличество попыток: " + str(result["attempts"]))


def tester():
    assert slow_search(range(1, 10),
                       8)["num"] == 8, "Slow search isn't working correctly"
    assert bin_search(range(1, 10),
                      8)["num"] == 8, "Binary search isn't working correctly"
    print("Тестирование завершено")


def user_input():
    min = int(input("Введите минимальное число: "))
    max = int(input("Введите максимальное число: "))
    num = int(input("Введите число от min до max: "))
    if min > max:
        print("min > max")
        return 0
    if num < min or num > max:
        print("Ваше число не входит в диапазон")
        return 0
    game(num, min, max)
