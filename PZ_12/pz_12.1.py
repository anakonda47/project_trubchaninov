# В матрице найти максимальный положительный элемент, кратный 4."""

import random

def main():
    try:
        size = int(input("Введите размер квадратной матрицы: "))
        matrix = [[random.randint(-20, 20) for _ in range(size)] for _ in range(size)]
        
        print("\nИсходная матрица:")
        for row in matrix:
            print(row)
            
    
        valid_elements = [val for row in matrix for val in row if val > 0 and val % 4 == 0]
        result = max(valid_elements) if valid_elements else None
        
        print(f"\nМаксимальный положительный элемент, кратный 4: {result}" if result 
              else "\nПоложительных элементов, кратных 4, в матрице нет.")
        
    except ValueError as e:
        print(e)

main()
