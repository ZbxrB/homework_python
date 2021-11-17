# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Warehouse:      # класс "Склад", дочерний по отношению к метеринскому "Подразделение"

    def __init__(self, current_office_equipments=None):
        if not current_office_equipments: # конструкция для создания пустого списка в случае, если для атрибута "current_office_equipments" не указано значение, путой список в __init__ указывать нельзя
            current_office_equipments = []
        self.current_office_equipments = current_office_equipments   # список, содержащий сведения об имеющейся на складе технике
        self.given_office_equipments = []      # список, содержащий сведения об отданной технике

    def get_equip(self, equip, division):     # метод, описывающий поведение при получении техники "equip" из подразделения "division" на склад
        self.given_office_equipments.remove(equip)      # из списка отданных удаляется экземпляр класса, дочернего классу "OfficeEquipment"
        self.current_office_equipments.append(equip)        # в список полученных добавляется экземпляр класса, дочернего классу "OfficeEquipment"
        equip.change_owner(self)    # в атрибут "собственник" экземпляра класса, дочернего классу "OfficeEquipment", записывается "склад"
        division.remove_equip(equip)  # обращаемся к методу класса "Accounting"

    def give_equip(self, equip, division):  # метод, описывающий поведение при получении техники "equip" из подразделения "division" на склад
        self.given_office_equipments.append(equip)  # из списка отданных удаляется экземпляр класса, дочернего классу "OfficeEquipment"
        self.current_office_equipments.remove(equip)  # в список полученных добавляется экземпляр класса, дочернего классу "OfficeEquipment"
        equip.change_owner(division)  # в атрибут "собственник" экземпляра класса, дочернего классу "OfficeEquipment", записывается "склад"
        division.add_equip(equip)  # обращаемся к методу класса "Accounting"


class Division:      # класс "Подразделение"
    def __init__(self, name, taking_office_equipments=None):
        if not taking_office_equipments:
            taking_office_equipments = []
        self.name = name
        self.taking_office_equipments = taking_office_equipments

    def remove_equip(self, equip):
        self.taking_office_equipments.remove(equip)     # из списка техники, имеющейся в подразделении, исключается экземпляр класса, дочерний классу "OfficeEquipment"

    def add_equip(self, equip):
        self.taking_office_equipments.append(equip)     # из списка техники, имеющейся в подразделении, исключается экземпляр класса, дочерний классу "OfficeEquipment"


class OfficeEquipment:      # материнский класс "Офисная техника"
    equip_type = None

    def __init__(self, name, quantity, owner):
        self.name = name    # атрибут, содержащий имя экземпляра класса

        while not str(quantity).isdigit():
            print('Entered value is not a number!')
            quantity = input('Enter the quantity: ')
        self.quantity = quantity  # атрибут, содержащий имя

        self.quantity = quantity


    def change_owner(self, owner):  # смена собственника для экземпляра класса "офисная техника"
        self.owner = owner

    def __repr__(self):
        return f'{self.equip_type}: {self.name} - {self.quantity} Pcs.'


class Printer(OfficeEquipment):     # класс "Принтер", дочерний по отношению к классу
    equip_type = 'printer'

    def __init__(self, name, quantity, color_print_type=True, owner=None):
        super(Printer, self).__init__(name, quantity, owner)
        self.color_print_type = color_print_type


class Scanner(OfficeEquipment):     # класс "Принтер", дочерний по отношению к классу
    equip_type = 'scanner'

    def __init__(self, name, quantity, scan_quality=800, owner=None):
        super(Scanner, self).__init__(name, quantity, owner)
        self.scan_quality = scan_quality


class Xerox(OfficeEquipment):     # класс "Принтер", дочерний по отношению к классу
    equip_type = 'xerox'

    def __init__(self, name, quantity, pages_per_minute=120, owner=None):
        super(Xerox, self).__init__(name, quantity, owner)
        self.pages_per_minute = pages_per_minute


a = Printer(input('Enter the name: '), input('Enter the quantity: '))
b = Scanner('KL90', 13)
c = Xerox('Pse1212-12', 3)
e = Printer('HP-A', 2)

accounting = Division('accounting')

warehouse = Warehouse([a, b, c, e])


print('In accounting: ', accounting.taking_office_equipments)
print('In warehouse: ', warehouse.current_office_equipments)

warehouse.give_equip(b, accounting)
warehouse.give_equip(e, accounting)
warehouse.give_equip(c, accounting)

print('In accounting: ', accounting.taking_office_equipments)
print('In warehouse: ', warehouse.current_office_equipments)

warehouse.give_equip(a, accounting)

print('In accounting: ', accounting.taking_office_equipments)
print('In warehouse: ', warehouse.current_office_equipments)