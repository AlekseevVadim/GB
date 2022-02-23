"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(num1, num2, num3):
    new_tuple = sorted((num1, num2, num3), reverse=True)
    return new_tuple[0] + new_tuple[1]


num1, num2, num3 = list(map(float, input('Введите три числа через пробел.\n').split()))
print("\n Сумма двух наибольших: ", my_func(num1, num2, num3))

