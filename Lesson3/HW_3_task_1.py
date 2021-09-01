"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""

def division(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль!"
    return round(num1 / num2, 3)


print("Введите 2 числа через пробел.")
num1, num2 = list(map(float, input().split()))
print(division(num1, num2))

