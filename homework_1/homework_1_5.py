revenue = int(input('Enter revenue: '))
costs = int(input('Enter costs: '))

if revenue < costs:
    print('The company has a loss')
else:
    print('The company has earnings')
    print(f'The profitability is {(revenue-costs)/revenue}')
    employer_count = int(input('Enter employer count: '))
    print(f'Profit per employee: {(revenue-costs)/revenue/employer_count}')