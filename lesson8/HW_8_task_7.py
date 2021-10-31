"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, re: int, im: int):
        self.re = re
        self.im = im

    def __str__(self):
        re_text = str(self.re)
        im_text = str(self.im)
        if self.im < 0:
            im_text = '(' + im_text + ')'
        return f"{re_text} + i * {im_text}"

    def __add__(self, other):
        re_result = self.re + other.re
        im_result = self.im + other.im
        return ComplexNumber(re_result, im_result)

    def __sub__(self, other):
        re_result = self.re - other.re
        im_result = self.im - other.im
        return ComplexNumber(re_result, im_result)

    def __mul__(self, other):
        re_result = self.re * other.re - self.im * other.im
        im_result = self.re * other.im + self.im * other.re
        return ComplexNumber(re_result, im_result)


# Проверка сложения и вычитания
a = ComplexNumber(8, - 9)
b = ComplexNumber(3, 4)
c = a + b
print(f"Сумма ({a}) и ({b}) равна ({c}).")
print(f"Разность ({a}) и ({b}) равна ({a - b}).")
# Проверка умножения
a = ComplexNumber(1, - 1)
b = ComplexNumber(3, 6)
print(f"Произведение ({a}) и ({b}) равно ({a * b}).")

