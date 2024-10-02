"""
Модуль для задания "калькулятор"
"""


def add(x, y):
    """Функция операции "сложение"""
    return x + y


def sub(x, y):
    """Функция операции "вычитание"""
    return x - y


def mul(x, y):
    """Функция операции "умножение"""
    return x * y


def div(x, y):
    """Функция операции "деление"""
    if y != 0:
        return x / y
    else:
        return "Деление на ноль"


def calc(oper, num1, num2):
    """Функция калькулятора"""
    result = 0
    if oper == '+':
        result = add(num1, num2)
    elif oper == '-':
        result = sub(num1,num2)
    elif oper == '*':
        result = mul(num1,num2)
    elif oper == '/':
        result = div(num1,num2)
    else:
        print("Неверная операция")
    print("Результат: " + str(result))
    return result

def user_input():
    oper = input("Операция (+ - * /): ")

    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    calc(oper, num1, num2)

def tester():
    assert calc("+",1,2)==3,"Calc isn't working correctly"
    assert calc("-",3,4)==-1,"Calc isn't working correctly"
    assert calc("/",4,2)==2,"Calc isn't working correctly"
    assert calc("*",4,0)==0,"Calc isn't working correctly"
    print("Тестирование завершено")