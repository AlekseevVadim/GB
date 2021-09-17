"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
 (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""
from sys import argv


def calculate(t, r, a):
    return t * r + a


file, time, rate, award = argv
time = int(time)
rate = int(rate)
award = int(award)

print(calculate(time, rate, award))
