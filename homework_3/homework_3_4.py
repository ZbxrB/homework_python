def my_func(x, y):
    result_my_func = x ** y
    return result_my_func


def my_func_2(x, y):
    result_my_func_2 = x
    i = 2
    while i <= y * (-1):
        result_my_func_2 *= x
        i += 1
    result_my_func_2 = 1 / result_my_func_2
    return result_my_func_2


x = float(input('Enter x: '))
y = int(input('Enter y: '))

print(my_func(x, y))
print(my_func_2(x, y))
