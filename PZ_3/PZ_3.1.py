#1. Дано трехзначное число. Проверить истинность высказывания: «Цифры данного 
#числа образуют возрастающую или убывающую последовательность». 
try:
    number = int(input("Введите трехзначное число"))
    a = number // 100
    b = (number // 10) % 10
    c = number % 10
    if a > b > c:
        print('True')
    elif a < b < c:
        print('True')
    else:
        print('False')
except ValueError:
    print("Ошибка: введите целое число")
