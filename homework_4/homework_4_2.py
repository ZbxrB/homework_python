basic_list = [12, 46, 13, 1, 11, 44, 45, 12, 10, 56, 3, 2, 4, 5]

parsed_list = [basic_list[i] for i in range(1, len(basic_list)) if basic_list[i] > basic_list[i-1]]

print(parsed_list)
