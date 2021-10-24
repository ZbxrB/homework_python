def data(first_name, second_name, year_of_birth, sity, email, number_of_phone):
    print(f'First name: {first_name}; Second name: {second_name}; Year of birth: {year_of_birth}; Sity: {sity}; Email: {email}; Number of Phone: {number_of_phone}')


data(
    first_name=input('Enter first name: '),
    second_name=input('Enter second name: '),
    year_of_birth=input('Enter the year of birth: '),
    sity=input('Enter the sity: '),
    email=input('Enter the email: '),
    number_of_phone=input('Enter the number of phone: ')
)
