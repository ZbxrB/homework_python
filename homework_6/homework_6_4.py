# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The car went")

    def stop(self):
        print('The car stopped')

    def turn(self, direction):
        print(f'The car turned on the {direction}')

    def show_speed(self):
        print(f'The Car speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed exceeded!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed exceeded!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'red', 'Toyota', False)
work_car = WorkCar(30, 'green', 'Mercedes', False)
sport_car = SportCar(120, 'white', 'Ferrari', False)
police_car = PoliceCar(90, 'blue', 'GAZ-21', True)

print(f'Speed {town_car.speed}, Color {town_car.color}, Name {town_car.name}, Is police {town_car.is_police}')
print(f'Speed {work_car.speed}, Color {work_car.color}, Name {work_car.name}, Is police {work_car.is_police}')
print(f'Speed {sport_car.speed}, Color {sport_car.color}, Name {sport_car.name}, Is police {sport_car.is_police}')
print(f'Speed {police_car.speed}, Color {police_car.color}, Name {police_car.name}, Is police {police_car.is_police}')

town_car.go()
work_car.stop()
town_car.show_speed()
sport_car.turn('left')
