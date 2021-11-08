# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass

    @abstractmethod
    def total_fabric_consumption(self, clothes_list):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_consumption(self):
        return self.v/6.5 + 0.5

    def total_fabric_consumption(self, coat_list):
        summ = 0
        for coat in coat_list:
            summ += coat.fabric_consumption
        return summ


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumption(self):
        return self.h * 2 + 0.3

    def total_fabric_consumption(self, suit_list):
        summ = 0
        for suit in suit_list:
            summ += suit.fabric_consumption
        return summ


coat = Coat(48)
suit = Suit(1.9)

print(coat.fabric_consumption)
print(suit.fabric_consumption)

print(coat.total_fabric_consumption([Coat(43), Coat(48)]))
