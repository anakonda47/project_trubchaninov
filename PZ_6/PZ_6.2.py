#Дан список A размера N. Сформировать новый список B того же
#размера, элементы которого определяются следующим образом:
#Bₖ = 2 * Aₖ, если Aₖ < 5,
#Aₖ / 2 в противном случае.

import random

try:
    #Базовые значения
    n = int(input("Введите длину списка:  "))
    a = [random.randint(0, 20) for i in range(n)]
    b = []
    #Перебор
    for i in a:
        if i < 5:
            b.append(i * 2)
        else:
            b.append(i / 2)
    #Вывод списков
    print("\nИсходный список:  ", a)
    print("\nИтоговый список:  ", b)
except ValueError:
    print("Ошибка")
