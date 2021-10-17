def my_func(num_1, num_2, num_3):
    min_num = num_1
    if num_2 < min_num:
        min_num = num_2
    elif num_3 < min_num:
        min_num = num_3
    else:
        result_my_func = num_2*num_3*num_1/min_num

    return result_my_func

input(my_func(
        int(input('Enter first number: ')),
        int(input('Enter second number: ')),
        int(input('Enter third number: '))
))