# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    data = None

    def __init__(self, data_str):
        self.data_str = data_str
        Data.data = self

    @classmethod
    def data_extraction(cls):
        separators = [' ', ';', ':', ',', '.', '-']
        data_dict = {}
        data_str = cls.data.data_str
        for separator in separators:
            if data_str.count(separator) > 0:
                separated_str = data_str.split(separator)
                data_dict.update(
                    {'Year': int(separated_str[0]), 'Month': int(separated_str[1]), 'Day': int(separated_str[2])})
                break
        return data_dict

    @staticmethod
    def validate(data_dict):
        if 0 < data_dict.get('Month') < 13:
            message = 'The  month number is correct.'
        else:
            message = 'The  month number is wrong.'
        return message


a = Data('1996,15,31')
print(a.data_extraction())
print(Data.validate(a.data_extraction()))

