# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    # конструктор, который создает объект, имеющий 2 атрибута, значения которых не являются постоянными атрибутами давнного класса,
    # а передаются при создании объекта данного класса слеюущим путем "имя_объекта = имя класса (значения атрибутов)"
    def __init__(self, length, width):
        self._length = length   # "_" в начале атрибута - защищенный модификатор доступа
        self._width = width

    # создаем метод, при вызове которого задаем 2 параметра (плотность асфальта и необходимую толщину слоя),
    # который возвращает массу асфальта, использую значения атрибутов, переданные при создании объектов данного класса
    def asphalt_mass(self, asphalt_density, thickness):
        return self._length * self._width * asphalt_density * thickness


new_road = Road(20, 5000)
print(new_road.asphalt_mass(25, 5))
