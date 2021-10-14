"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

"""


class Cell:

    def __init__(self, num: int):
        self.num = num

    def __str__(self):
        return f"Эта клетка имеет {self.num} ячеек."

    def __add__(self, other):
        try:
            other.num
        except AttributeError:
            print("Оба слагаемых должны иметь класс Cell.")
        else:
            return Cell(self.num + other.num)

    def __sub__(self, other):
        try:
            other.num
        except AttributeError:
            print("Оба аргумента должны иметь класс Cell.")
        else:
            result = self.num - other.num
            if result > 0:
                return Cell(result)
            else:
                print("Уменьшение клетки не может приводить к неположительному результату.")

    def __mul__(self, other):
        try:
            other.num
        except AttributeError:
            print("Оба аргумента должны иметь класс Cell.")
        else:
            return Cell(self.num * other.num)

    def __truediv__(self, other):
        try:
            other.num
        except AttributeError:
            print("Оба аргумента должны иметь класс Cell.")
        else:
            result = self.num // other.num
            if result > 0:
                return Cell(result)
            else:
                print("Уменьшение клетки не может приводить к неположительному результату.")

    def make_order(self, count):
        result = ("*" * count + '\n') * (self.num // count) + "*" * (self.num % count)
        if self.num % count == 0:
            result = result[:-1]
        return result


A = Cell(4)
B = Cell(6)
C = A + 8
C = A + B
print(C)
print(C.make_order(3))
D = B - 9
D = B - Cell(6)
D = B - A
print(D)
print(D.make_order(4))
E = A * 9
E = A * B
print(E)
print(E.make_order(8))
F = A / B
F = B / A
print(F)
print(F.make_order(3))