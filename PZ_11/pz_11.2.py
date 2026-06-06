#Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
получить новый список, в котором длина слов не превышает 5 символов."""

try:
    
    def filter_names(names_list):
        for name in names_list:
            if len(name) <= 5:
                yield name

    input_list = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
    print("Исходный список:", input_list)

    result_list = list(filter_names(input_list))
    print("Новый список (длина слов не превышает 5 символов):", result_list)

except ValueError as e:
    print(e)
