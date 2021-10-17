command = ''

sum = 0

while command != 's':
    # print(f'Summ = : {sum}')
    numbers_list = input('Enter the numbers separated by a space or a symbol "s" to stop typing: ').split()
    for el in numbers_list:
        if el == 's':
            command = el
            break
        sum += float(el)
    print(f'Summ = {sum}')
