#В  последовательности  на  n  целых  элементов  в  последней  ее  половине  найти 
#сумму элементов."""

import random

def main():
    try:
        a = int(input("Напишите кол-во чисел\n"))
        
     
        b = [random.randint(-10, 10) for _ in range(a)]
        print("Сам список:", b)
        
        half_index = len(b) // 2
        second_half = b[half_index:]
        print("Последняя половина элементов:", second_half)
        
        total_sum = sum(second_half)
        print(f"Сумма элементов в последней половине: {total_sum}")

    except ValueError as e:
        print(f"Произошла ошибка: {e}")

main()
