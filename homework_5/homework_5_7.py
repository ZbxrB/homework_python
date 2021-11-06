# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#   Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#   Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#   Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json


profit_firms_dict = {}
count = 0
aver_profit = 0

with open('data_of_firms.txt', 'r') as file:
    for line in file.readlines():
        count += 1
        line_split = line.split()
        profit = float(line_split[2]) - float(line_split[3])
        profit_firms_dict.update({line_split[0]: profit})
        aver_profit += profit

aver_profit_dict = {"average_profit": aver_profit / count}

profit_list = [ profit_firms_dict, aver_profit_dict]

with open('profit_json_file.json', 'w') as write_json:
    json.dump(profit_list, write_json)

