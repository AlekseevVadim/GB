"""
    Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
    Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
    Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""


class NotInStorage(Exception):
    def __init__(self, txt: str = "Объекта нет в хранилище!"):
        self.txt = txt


class Storage:
    def __init__(self, name: str):
        self.name = name
        self.storage = {}

    def to_give(self, address, equipment_take: list):
        for stuff in equipment_take:
            if self.storage.get(str(stuff)) is None:
                raise NotInStorage(f'Объекта {str(stuff)} нет в хранилище!')
            elif equipment_take.count(stuff) > self.storage.get(str(stuff)):
                raise NotInStorage(f'Объектов {str(stuff)} не достаточно для выдачи!')

        for stuff in equipment_take:
            self.storage[str(stuff)] -= 1
            if self.storage[str(stuff)] == 0:
                self.storage.pop(str(stuff))
        address.to_save(equipment_take)

    def to_save(self, equipment_save: list):
        for stuff in equipment_save:
            if self.storage.get(str(stuff)) is not None:
                self.storage[str(stuff)] += 1
            else:
                self.storage[str(stuff)] = 1

    def __str__(self):
        return f'{self.name}, содержимое:\n{self.storage}'


class OfficeEquipment:
    def __init__(self, name_type: str, brand: str, model: str):
        self.name_type = name_type
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.name_type} {self.brand} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, speed_print: int):
        super().__init__('Принтер', brand, model)
        self.speed_print = speed_print

    def print_some(self, obj):
        print(f'Печать {obj} со скоростью {self.speed_print}')

    @property
    def print_test(self):
        print(f'Пробная печать. {self}, скорость печати - {self.speed_print}')


class Scanner(OfficeEquipment):
    def __init__(self, brand: str, model: str, list_format: set):
        super().__init__('Сканер', brand, model)
        self.list_format = list_format

    def scan_some(self, obj, format: str = 'A4'):
        if format not in self.list_format:
            print(f'Не верно задан формат! Доступно: {self.list_format}')
        else:
            print(f'Сканирование {obj} в формате {format}')


class Xerox(Scanner, Printer):
    def __init__(self, brand: str, model: str, speed_print: int, list_format: set):
        OfficeEquipment.__init__(self, 'Ксерокс', brand, model)
        self.speed_print = speed_print
        self.list_format = list_format


A = Storage('Склад А')
B = Storage('Отдел кадров')
a1 = Printer('Samsung', 'X340', 1500)
a2 = Printer('Sony', 'P45', 1000)
b1 = Scanner('Sony', 'S67', {'A4', 'A3', 'A5'})
c1 = Xerox('Philips', 'X5', 1200, {'A4', 'A3'})

A.to_save([a1]*5 + [a2]*3 + [b1]*8)
print(A)
A.to_give(B, [a1]*2 + [b1]*4)
print(A)
print(B)
B.to_save([c1])
try:
    B.to_give(A, [c1]*2)
except NotInStorage:
    print('Выдача невозможна!')
print(A)
print(B)

a1.print_some('Note_a1')
b1.scan_some('Note_b1')
c1.print_some('Note_c1')
c1.scan_some('Note_c1', 'A3')

a1.print_test
c1.print_test
