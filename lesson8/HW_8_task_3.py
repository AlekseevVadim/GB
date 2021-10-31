"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotNumberError(ValueError):
    def __init__(self, txt: str = "Хранение объектов нечислового формата в объекте данного класса недопустимо!"):
        self.txt = txt


def list_num_validation(add_obj: str):
    result = ''
    if add_obj[0] == '-':
        result += '-'
        add_obj = add_obj[1:]
    num_list = add_obj.split('.')
    if len(num_list) > 2:
        raise NotNumberError
    for num_part in num_list:
        if not num_part.isnumeric():
            raise NotNumberError
        else:
            result += num_part + '.'
    return float(result[:-1])


result = []
print("Создание списка запущено. Для остановки введите: stop")
print("Введите число (float) для внесения в список. Примеры написания: 9.0, -8.7, ...")
inp = input()
while inp != 'stop':
    try:
        num = list_num_validation(inp)
    except NotNumberError:
        print(f'Допустим ввод только чисел! {inp} - не может быть преобразовано в число.')
    else:
        result.append(num)
    print("Введите число (float) для внесения в список.")
    inp = input()
print(f"Получен список:\n{result}")
