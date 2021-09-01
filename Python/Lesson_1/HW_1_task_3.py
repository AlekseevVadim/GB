
# coding: utf-8


# ЗД 3
"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

"""

n = input('Enter your "n": ')
result = int(n) + int(n * 2) + int(n * 3)
print('Your result: {} + {} + {} = {}'.format(int(n), int(n * 2), int(n * 3), result))
