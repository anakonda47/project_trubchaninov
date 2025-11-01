try:
    number = int(input("Введите целое число"))
    if number > 0:
        number = number + 1
    else:
        number = number - 2
    print("Получено число",number)

except ValueError:
    print("Ошибка: введите целое число")

