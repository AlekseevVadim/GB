
# coding: utf-8

# ЗД 1
"""
1. Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните
в переменные, выведите на экран.

"""

a = 78
b = 43
c = 'integer'
d = 77.43
e = 'float'

print('Example')
print("{} and {} - {}, {} - {}".format(a, b, c, d, e))
print('Repeat with other numbers!')

a = int(input('\nEnter a: '))
b = int(input('Enter b: '))
d = float(input('Enter d:'))
f_name = input('Enter your name: ')
l_name = input('Enter your surname: ')

print(f'\nResult of {f_name} {l_name}')
print("{} and {} - {}, {} - {}".format(a, b, c, d, e))
print('Repeat with other numbers!')
