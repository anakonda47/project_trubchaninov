#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

Содержимое первого файла:
Четные элементы:
Произведение четных элементов:
Минимальный элемент:

Содержимое второго файла:
Нечетные элементы:
Количество нечетных элементов:
Сумма нечетных элементов:"""

try:
    # --- ОБРАБОТКА ПЕРВОГО ФАЙЛА ---
    list = []
    with open("text1.txt", "r", encoding="utf-8") as f:
        for i in f.read().split(","):
            list.append(int(i))
            
   
    even_elements = [i for i in list if i % 2 == 0]
    

    mult_even = 1
    for i in even_elements:
        mult_even *= i
    if not even_elements:  # на случай если четных нет
        mult_even = 0
        
  
    min_element = min(list)

   
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"Содержимое первого файла: {list}\n\n"
                f"Четные элементы: {even_elements}\n\n"
                f"Произведение четных элементов: {mult_even}\n\n"
                f"Минимальный элемент: {min_element}\n\n")


    # --- ОБРАБОТКА ВТОРОГО ФАЙЛА ---
    list = []  
    with open("text2.txt", "r", encoding="utf-8") as f:
        for i in f.read().split(","):
            list.append(int(i))
            

    odd_elements = [i for i in list if i % 2 != 0]
    
 
    count_odd = len(odd_elements)
    sum_odd = sum(odd_elements)

    
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(f"Содержимое второго файла: {list}\n\n"
                f"Нечетные элементы: {odd_elements}\n\n"
                f"Количество нечетных элементов: {count_odd}\n\n"
                f"Сумма нечетных элементов: {sum_odd}")

except ValueError as e:
    print(f"Произошла ошибка: {e}")
