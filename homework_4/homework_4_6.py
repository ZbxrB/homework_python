from itertools import count, cycle

init_numb = int(input('Enter the initial number: '))
numb_list = []

for el in count(init_numb):
    if el > init_numb * 2:
        break
    else:
        numb_list.append(el)

print(numb_list)

i = 0
for el in cycle(numb_list):
    if i > 2 * len(numb_list):
        break
    else:
        print(el)
        i += 1