"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
name_file = "for_task_5.txt"
with open(name_file, 'w', encoding="utf-8") as new_file:
    print("Введите числа для записи в файл через пробел.")
    print(input(), file=new_file)
with open(name_file, 'r', encoding="utf-8") as new_file:
    result = sum([float(x.rstrip()) for x in new_file.read().split()])
    print(round(result, 3))