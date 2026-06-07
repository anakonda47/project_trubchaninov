 #2. Создайте класс "Фигура", который содержит метод расчета площади фигуры.
 #Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
 #"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры."""

class Figure:
    def area(self):
        return 0


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


try:
    square = Square(side=5)
    rectangle = Rectangle(width=4, height=6)

    print("Квадрат:")
    print(f"Площадь: {square.area()}")

    print("\nПрямоугольник:")
    print(f"Площадь: {rectangle.area()}")

except ValueError as e:
    print(e)
