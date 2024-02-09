'''
2) Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
Реализуйте метод calculate_area(), который возвращает площадь прямоугольника.
'''


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


a = Rectangle(width=2, height=2)
print(a.calculate_area())
b = Rectangle(width=10, height=5)
print(b.calculate_area())
