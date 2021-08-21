
# coding: utf-8

# ЗД 2
"""
2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.

"""

num = int(input('Enter time in seconds: '))
time_sec = num
time_hours = time_sec // 3600
time_sec = time_sec % 3600
time_min = time_sec // 60
time_sec = time_sec % 60
print(f'Time is {time_hours:02}:{time_min:02}:{time_sec:02}')
print(f'Check! --> {num == time_hours * 3600 + time_min * 60 + time_sec}')
