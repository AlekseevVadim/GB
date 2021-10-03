"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручки.")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандаша.")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркера.")


a = Stationery('Ножницы')
print("a - ", a.title)
a.draw()
b = Pencil('Зеленый карандаш')
print("b - ", b.title)
b.draw()
c = Handle('Черный маркер')
print("c - ", c.title)
c.draw()
d = Pen('Шариковая ручка')
print("d - ", d.title)
d.draw()
