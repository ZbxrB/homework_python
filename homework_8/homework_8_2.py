# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ErrorDivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


try:
    x = int(input('Enter the number: '))
    y = int(input('Enter the number: '))
    if y == 0:
        raise ErrorDivisionByZero('Error! Division by zero!')
except ErrorDivisionByZero as err:
    print(err)
else:
    print(f'The division result is {x / y}')
