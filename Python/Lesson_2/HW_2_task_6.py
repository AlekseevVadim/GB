"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}

Важно!
При отправке домашнего задания обязательно нажимайте галочку "Показать задание ментору".
"""

products = []
command = None
i = 1
while command != 'stop':
    print('For view Products - enter "output".', end =' ')
    print('For analyze Products - enter "analyze".')
    print('For add product - enter "add".', end =' ')
    print('For exit - enter "stop".\n')
    command = input()
    print()
    if command == 'output':
        for item in products:
            print(item)
        print()
    elif command == 'add':
        print('Enter value of "Название".')
        name = input()
        print('Enter value of "Цена".')
        price = int(input())
        print('Enter value of "Количество".')
        amount = int(input())
        print('Enter value of "Ед.".')
        units = input()
        products.append(
            (i, {"название": name, "цена": price, "количество": amount, "eд": units})
        )
        i += 1
        print('Adding succeeded.\n')
    elif command == 'analyze':
        analyze = dict(
            название = [products[it][1].get("название") for it in range(i - 1)],
            цена = [products[it][1].get("цена") for it in range(i - 1)],
            количество = [products[it][1].get("количество") for it in range(i - 1)],
            ед = list(set([products[it][1].get("eд") for it in range(i - 1)]))
        )
        print(analyze, '\n')

