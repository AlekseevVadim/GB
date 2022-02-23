"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
name_file = "for_task_3.txt"
with open(name_file, 'r', encoding="utf-8") as new_file:
    str_list = new_file.readlines()

str_list = [x.rstrip().split() for x in str_list if x != '\n']
# print(str_list)
fam_less20 = ''
med_salary = 0
num_emp = len(str_list)
for i in range(num_emp):
    str_list[i][1] = float(str_list[i][1])
    if (str_list[i][1]) < 20000:
        fam_less20 += str_list[i][0] + ' '
    med_salary += str_list[i][1] / num_emp

print("Фамилии сотрудников с доходом менее 20 тыс.:")
print(fam_less20)
print(f"Средняя величина дохода сотрудников - {med_salary:.3f}")
