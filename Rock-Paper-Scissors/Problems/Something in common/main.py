def calculate_linear(k, b, x):
    y = k * x + b
    print("Value of the function equals", y)
    return y


def calculate_quadratic(a, b, c, x):
    y = (a * x * x) + (b * x) + c
    print("Value of the function equals", y)
    return y


# create function common_part
def common_part(y):
    print("Value of the function equals", y)
    return y
