"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла:
firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""
import json

name_file_r = "for_task_7.txt"
name_file_w = "for_task_7.json"
firm_dict = {}
atr_dict = {}
average_profit = 0
with open(name_file_r, 'r', encoding="utf-8") as new_file:
    i = 0
    for line in new_file:
        new_list = [x.rstrip() for x in line.split()]
        proceeds = int(new_list[2]) - int(new_list[3])
        firm_dict.update([(new_list[0], proceeds)])
        if proceeds >= 0:
            average_profit += proceeds
            i += 1
    atr_dict.update([('average_profit', average_profit / i)])
json_file = [firm_dict, atr_dict]
print(json_file)

with open(name_file_w, "w") as new_file:
    json.dump(json_file, new_file)
