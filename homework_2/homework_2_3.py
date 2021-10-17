month = int(input('Enter the month: '))

month_name_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month_name_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5:  'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

while month > 12:
    month = int(input('Enter the month number from 1 to 12: '))

print(month_name_list[month-1])
print(month_name_dict.get(month))