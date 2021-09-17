"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

print("Первый скрипт")
print("Введите число до 10 для генерации целых чисел")
N = int(input())

for x in count(N):
    if x > 10:
        break
    print(x)

print("Второй скрипт")
print("Введите список через пробел для повтора элементов")
new_list = list(input().split())

c = 0
for x in cycle(new_list):
    if c == 5:
        break
    print(x)
    c += 1