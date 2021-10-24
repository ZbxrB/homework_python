from functools import reduce


def multi(el_1, el_2):
    return el_1 * el_2


num_list = [el for el in range(100, 1002, 2)]

print(num_list)
print(reduce(multi, num_list))
