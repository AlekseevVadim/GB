"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.

"""
name_file = "for_task_2.txt"
with open(name_file, 'r', encoding="utf-8") as new_file:
    str_list = new_file.readlines()
    str_list = [x.rstrip() for x in str_list]

num_str = len(str_list)
print(f"В файле {name_file} кол. строк - {num_str} шт.")
for i in range(num_str):
    print(f"В {i + 1} строке слов - {len(str_list[i].split())}")
