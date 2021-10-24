def divide():
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))

    while num_2 == 0:
        num_2 = int(input('It is impossible to divide by zero, enter second number not equal to zero: '))

    result_divide = num_1/num_2
    return result_divide

print(divide())