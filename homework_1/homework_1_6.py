a = int(input('Enter result of the first day: '))
b = int(input('Enter desired result: '))

day = 1
while a < b:
    a *= 1.1
    day += 1

print(f'The result will be achieved on day {day}')