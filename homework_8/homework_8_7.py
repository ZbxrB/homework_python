# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.
import math


class Complex:
    def __init__(self, complex):
        self.complex = complex

    def __add__(self, other):
        x = int(self.complex[0]) + other.complex[0]
        y = int(self.complex[1]) + other.complex[1]
        return Complex([x, y])

    def __mul__(self, other):
        x = int(self.complex[0]) * int(other.complex[0]) - int(self.complex[1]) * int(other.complex[1])
        y = int(self.complex[0]) * int(other.complex[1]) + int(other.complex[0]) * int(self.complex[1])
        return Complex([x, y])

    def __str__(self):
        sign = '+'
        if int(self.complex[1]) == 0:
            sign = ''
        elif int(self.complex[1]) < 0:
            sign = '-'
        return f'{self.complex[0]} {sign} {abs(self.complex[1])}i'


a = Complex([1, 2])
b = Complex([4, -3])
print(b + a)
print(a * b)
