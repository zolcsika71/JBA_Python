class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.get_perimeter()
