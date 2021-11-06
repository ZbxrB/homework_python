# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

content = []
with open('salary.txt', 'r') as file:
    for el in file.readlines():                 # перебираем список, элементами которого являются строки файла и учетом элемента перехода "\n"
        new_el = el.replace('\n', '')        # вырезаем из стоки элемент перехода на другую строку "\n"
        content.append(new_el.split())

count = 0
summ = 0
for el in content:
    count += 1
    summ += int(el[1])
    if int(el[1]) < 20000:
        print(f'Employee {el[0]} has a salary less than 20000')

print(f'The average salary is {summ / count:.2f}')

