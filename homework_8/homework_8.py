# Задача с классом JSON

import json
with open("zadacha.json") as f:
    date = json.loads(f.read())
    keys = list(date.keys())
    values = list(date.values())

def __init__(self,values,keys,date):

        self.values = values
        self.keys = keys
        self.date = date


    def values(self):
        print("values")

    def keys(self):
        print("keys")

    def date(self):
        print("date")


# Задача с тругольником
class Rectangle:
    def __init__(self, coord: (int, int), width: int, height: int):
        self.a, self.width, self.height = coord, width, height

    @property
    def b(self) -> (int, int):
        return self.a[0] + self.width, self.a[1]

    @property
    def c(self) -> (int, int):
        return self.b[0], self.b[1] - self.height

    @property
    def d(self) -> (int, int):
        return self.a[0], self.a[1] - self.height

    @property
    def perimeter(self) -> int:
        return (self.width + self.height) * 2

    @property
    def area(self) -> int:
        return self.width * self.height

    def __str__(self) -> str:
        return (f"Rectangle(width={self.width}, height={self.height}, "
                f"perimeter={self.perimeter}, area={self.area})\n"
                f"    Rectangle.a: x={self.a[0]}, y={self.a[1]}\n"
                f"    Rectangle.b: x={self.b[0]}, y={self.b[1]}\n"
                f"    Rectangle.c: x={self.c[0]}, y={self.c[1]}\n"
                f"    Rectangle.d: x={self.d[0]}, y={self.d[1]}\n")


rect = Rectangle((0, 5), 5, 10)
print(rect)
rect.a = (5, 5)
print(rect)