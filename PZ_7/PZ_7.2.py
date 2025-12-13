#Даны строки S, S1 и S2. Заменить в строке S все вхождения строки Si на строку S2.
try:
    S = input()
    S1 = input()
    S2 = input()

    result = S.replace(S1, S2)
    print(result)
except ValueError:
    print("Ошибка")
