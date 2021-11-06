number = int(input('Enter integer number: '))

max = number % 10
number = number // 10
while number > 1:
        if max == 9:
               break
        elif max < number % 10:
                max = number % 10
        number = number // 10

print(f'Max count is {max}')