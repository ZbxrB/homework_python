# Создать(программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random


def num_generator():
    set_of_num = ''
    n = random.randint(3, 10)
    for el in range(n):
        set_of_num += str(random.random()*10) + ' '
    return set_of_num


with open('set_of_numbers.txt', 'w') as file:
    file.write(num_generator())

summa = 0
with open('set_of_numbers.txt', 'r') as file:
    for el in file.readline().split():
        summa += float(el)

print(summa)

