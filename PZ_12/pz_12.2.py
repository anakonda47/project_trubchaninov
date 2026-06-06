2. В квадратной матрице все элементы, не лежащие на главной диагонали,
увеличить в 2 раза."""

import random

def main():
    try:
        size = int(input("Введите размер квадратной матрицы: "))
        matrix = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
        
        print("\nИсходная матрица:")
        for row in matrix:
            print(row)
            
        # пересчет элементов вне главной диагонали
        result_matrix = [
            [row[j] * 2 if i != j else row[j] for j in range(size)]
            for i, row in enumerate(matrix)
        ]
        
        print("\nМатрица после изменения:")
        for row in result_matrix:
            print(row)
        
    except ValueError as e:
        print(e)

main()
