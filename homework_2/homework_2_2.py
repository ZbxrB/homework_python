count_list = []

el = input('Введите значение, которое хотите добавить в список, или "end", если хотите прекратить ввод элементов списка: ')
while el != 'end':
    count_list.append(el)
    el = input('Введите значение, которое хотите добавить в список, или "end", если хотите прекратить ввод элементов списка: ')

lenght = len(count_list)

i = 0
while i < lenght - 1:
    count_list.insert(i, count_list[i+1])
    del count_list[i+2]
    i += 2

print(count_list)
