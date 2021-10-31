"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, dt_str: str):
        dt_tuple = Date.to_dmy(dt_str)
        if Date.date_valid(dt_tuple):
            self.day = dt_tuple[0]
            self.month = dt_tuple[1]
            self.year = dt_tuple[2]
        else:
            raise Exception("Неверный формат даты.")

    @classmethod
    def to_dmy(cls, obj: str):
        dt_list = list(map(int, obj.split("-")))
        return dt_list[0], dt_list[1], dt_list[2]

    @staticmethod
    def date_valid(dmy):
        md_dict = {1: 31, 2: 28, 3: 31, 4: 30,
                 5: 31, 6: 30, 7: 31, 8: 31,
                 9: 30, 10: 31, 11: 30, 12: 31}
        if dmy[1] not in md_dict:
            return False
        elif (dmy[0] < 1) or (dmy[0] > md_dict[dmy[1]]):
            if (dmy[1] == 2) and dmy[0] == 29:
                return True
            else:
                return False
        else:
            return True

    def __str__(self):
        return f"День - {self.day}, месяц - {self.month}, год - {self.year}."


a = '11-06-1996'
b = '36-98-1997'
a_dt = Date(a)
# b_dt = Date(b) # приведёт к ошибке
print(a_dt)
a_spl = Date.to_dmy(a)
b_spl = Date.to_dmy(b)
print(a_spl, b_spl)
print(Date.date_valid(a_spl), Date.date_valid(b_spl))
