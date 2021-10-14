"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def estimation(self):
        pass

    @abstractmethod
    def parameter(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def estimation(self):
        return round(self.__size / 6.5 + 0.5, 3)

    @property
    def parameter(self):
        return self.__size


class Suit(Clothes):
    def __init__(self, name: str, height: float):
        self.name = name
        self.__height = height

    @property
    def estimation(self):
        return 2 * self.__height + 0.3

    @property
    def parameter(self):
        return self.__height


A = Suit("Italy №3", 189.5)
B = Coat("Vintage", 67)
print(f"Костюм - {A.name}, рост - {A.parameter}, расход ткани - {A.estimation}")
print(f"Пальто - {B.name}, размер - {B.parameter}, расход ткани - {B.estimation}")

