"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

print("Введите числа через пробел")
list1 = list(map(int, input().split()))

list2 = [list1[i] for i in range(len(list1)) if list1[i] not in
         (list1[j] for j in range(len(list1)) if j != i)
         ]
print(list2)