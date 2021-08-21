
# coding: utf-8


# ЗД 4
"""
4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.

"""

num = int(input('Enter your number: '))
i = num
result = 0
while i != 0:
    a = i % 10
    if a > result:
        result = a
    i = i // 10
print(f'Largest digit in {num}: {result}')
