def int_func(word):
    word = word.capitalize()
    return word


words_list = input('Enter words separated by a space: ').split()
words_str =''
for index, el in enumerate(words_list):
    words_list.insert(index, int_func(el))
    words_list.pop(index+1)
    words_str += f'{words_list[index]} '

print(words_str)
