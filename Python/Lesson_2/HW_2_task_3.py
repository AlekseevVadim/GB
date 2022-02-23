"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
# через list
month = int(input())
months = ['зима', 'весна', 'лето', 'осень']
if month in (12, 1, 2):
    print(f"{month} месяц - {months[0]}")
elif month in (3, 4, 5):
     print(f"{month} месяц - {months[1]}")
elif month in (6, 7, 8):
     print(f"{month} месяц - {months[2]}")
elif month in (9, 10, 11):
     print(f"{month} месяц - {months[3]}")
        
# через dict
new_dict = {'зима': (12, 1, 2) , 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for key in new_dict.keys():
    if month in new_dict.get(key):
        print(f"{month} месяц - {key}")

