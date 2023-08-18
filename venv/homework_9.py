import math


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))


class Round(Figure):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2



figures = [
    Triangle(3, 4, 5),
    Round(7),
    Triangle(6, 8, 10),
    Round(5)
]

total_perimeter = 0
total_area = 0

for figure in figures:
    total_perimeter += figure.perimeter()
    total_area += figure.area()

print("Общий периметр:", total_perimeter)
print("Общая площадь:", total_area)
