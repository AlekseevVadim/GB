"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"Car {self.name} (color - {self.color}) went.")

    def stop(self):
        print(f"Car {self.name} (color - {self.color}) stopped.")

    def turn(self, direction):
        print(f"Car {self.name} (color - {self.color}) turned {direction}.")

    def show_speed(self):
        print(f"Speed of {self.name} (color - {self.color}) is {self.speed}.")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Speed of {self.name} (color - {self.color}) is {self.speed}. More than 60 - reduce speed!")
        else:
            print(f"Speed of {self.name} (color - {self.color}) is {self.speed}.")


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Speed of {self.name} (color - {self.color}) is {self.speed}. More than 40 - reduce speed!")
        else:
            print(f"Speed of {self.name} (color - {self.color}) is {self.speed}.")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


car_1 = Car(67, 'red', 'Mercedes')
print('car_1 - ', car_1.name, car_1.speed, car_1.color, car_1.is_police)
car_1.go()
car_1.show_speed()
car_1.turn('left')
car_1.stop()

car_2 = TownCar(68, 'yellow', 'BMW')
print('car_2 - ', car_2.name, car_2.speed, car_2.color, car_2.is_police)
car_2.go()
car_2.show_speed()
car_2.speed = 50
car_2.show_speed()
car_2.turn('right')
car_2.stop()

car_3 = SportCar(89, 'pink', 'Subaru')
print('car_3 - ', car_3.name, car_3.speed, car_3.color, car_3.is_police)
car_3.go()
car_3.show_speed()
car_3.speed = 70
car_3.show_speed()
car_3.turn('right')
car_3.stop()

car_4 = WorkCar(90, 'green', 'Renault')
print('car_4 - ', car_4.name, car_4.speed, car_4.color, car_4.is_police)
car_4.go()
car_4.show_speed()
car_4.speed = 30
car_4.show_speed()
car_4.turn('right')
car_4.stop()

car_5 = PoliceCar(90, 'white', 'Nissan')
print('car_5 - ', car_5.name, car_5.speed, car_5.color, car_5.is_police)
car_5.go()
car_5.show_speed()
car_5.speed = 30
car_5.show_speed()
car_5.turn('right')
car_5.stop()
