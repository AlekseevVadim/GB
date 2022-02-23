"""
1. Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    __color = 'красный'

    def running(self):
        flag_on = True
        color_dict = {'красный': 7, 'жёлтый': 2, 'зелёный': 10}
        color_list = list(color_dict.keys())
        print(color_list)
        time_on = 0
        while flag_on:
            print(f"Цвет светофора - {self.__color}, время ожидания - {color_dict.get(self.__color)}")
            sleep(color_dict.get(self.__color))
            time_on += color_dict.get(self.__color)
            if time_on > 20:
                flag_on = False
            else:
                i = color_list.index(self.__color)
                if i == 2:
                    i = -1
                self.__color = color_list[i + 1]


a = TrafficLight()
a.running()
