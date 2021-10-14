"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, param: list):
        max_length = len(sorted(param, key=lambda x: len(x))[-1])
        self.row = len(param)
        self.col = max_length
        [x.extend([0] * (self.col - len(x))) for x in param]
        self.param = param

    def __str__(self):
        result = '\n'
        for x in self.param:
            result += str(x) + '\n'
        return result

    def __add__(self, other):
        try:
            other.param
        except AttributeError:
            print("Оба слагаемых должны иметь класс Matrix.")
        else:
            if (self.col == other.col) and (self.row == other.row):
                result = [[m + n for m, n in zip(self.param[i], other.param[i])] for i in range(self.col)]
                return Matrix(result)
            else:
                print(f"Сложение невозможно для матриц разных размеров: {self.col}x{self.row} и {other.col}x{other.row}")


a = Matrix([[1, 2, 6], [3, 4, 7], [5, 6]])
a1 = Matrix([[1, 2, 6], [3, 4, 7], [0, 0]])
b = Matrix([[1, 2], [3, 4, 7, 9]])

print(f"Число столбцов матрицы a - {a.col}, число строк - {a.row}.")
print(f"Число столбцов матрицы b - {b.col}, число строк - {b.row}.")
print('Это матрица a -', a, 'а это матрица b -', b)

a1 = Matrix([[1, 2, 6], [3, 4, 7], [0, 0]])
# a1 = Matrix([[1, 2, 6], [3, 4, 7]])
c = a + a1
print("a + a1 =", c)
