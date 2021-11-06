# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

new_file = open('new_file.txt', 'w')

command = True
while command != False:
    content = input('Ввведите данные для записи в файл: ')
    if content == '':
        new_file.writelines(content)
        break
    new_file.writelines(content + '\n')

new_file.close()