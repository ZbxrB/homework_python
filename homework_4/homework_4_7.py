def fact(n):
    c = 1
    for i in range(1, n+1):
        c *= i
        yield c

n = int(input('Enter the number: '))

i = 1
for el in fact(n):
    print(f"{i}! = {el}")
    i += 1
