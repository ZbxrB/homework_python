words_str = input('Enter the words separated by a space: ')

words_list = words_str.split()

i = 0
for el in words_list:
    if len(el) > 10:
        print(f'line {i+1}: {el[:10]}')
    else:
        print(f'line {i + 1}: {el}')
    i += 1