rat_list = [9, 8, 4, 3, 3, 2, 1, 1, 0]

rating = int(input('Enter the rating: '))
there_is = False

for index, el in enumerate(rat_list):
    if rating > el:
        rat_list.insert(index, rating)
        there_is = True
        break

if not there_is:
    rat_list.append(rating)

print(rat_list)