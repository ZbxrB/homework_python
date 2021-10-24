base_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

parsed_list = [base_list[i] for i in range(0, len(base_list)) if base_list.count(base_list[i]) == 1]

print(parsed_list)
