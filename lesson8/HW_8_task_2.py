"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class DivisionZeroError(Exception):
    def __init__(self, txt: str = "Деление на ноль недопустимо!"):
        self.txt = txt


print("Введите делимое (float) и делитель (float) через пробел.")
try:
    a, b = map(float, input().split())
    if b == 0:
        raise DivisionZeroError()
    result = a / b
except ValueError:
    print("Введен неверный формат.")
except DivisionZeroError as err:
    print(err.txt)
else:
    print(f"Результат деления: {round(result, 3)}")
