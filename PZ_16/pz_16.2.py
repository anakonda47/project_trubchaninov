#2. Создайте класс "Фигура", который содержит метод расчета площади фигуры.
 #Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
 #"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры."""
class Figure:
    def __init__(self, side_a=0, side_b=0):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b


class Square(Figure):
    def __init__(self, side):
        super().__init__(side_a=side, side_b=side)


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(side_a=width, side_b=height)


try:
    square = Square(side=5)
    rectangle = Rectangle(width=4, height=6)

    print("Квадрат:")
    print(f"Площадь: {square.area()}")

    print("\nПрямоугольник:")
    print(f"Площадь: {rectangle.area()}")

except ValueError as e:
    print(e)
