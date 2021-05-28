class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.get_area()

    def get_area(self):
        print(f'{self.a * self.b * 0.5}')


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

if input_c ** 2 == input_a ** 2 + input_b ** 2:
    triangle = RightTriangle(input_c, input_a, input_b)
else:
    print('Not right')
