"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
name_file_r = "for_task_4_in.txt"
name_file_w = "for_task_4_out.txt"
num_dict = {'One':'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open(name_file_r, 'r', encoding="utf-8") as file_r:
    with open(name_file_w, 'w', encoding="utf-8") as file_w:
        for line in file_r:
            line_list = [x.rstrip() for x in list(line.split(' — '))]
            line_list[0] = num_dict.get(line_list[0])
            print(*line_list, sep=' — ', file=file_w)

