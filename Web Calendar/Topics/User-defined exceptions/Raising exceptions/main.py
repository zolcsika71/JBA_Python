class NegativeSumError(Exception):
    pass


def sum_with_exceptions(a, b):
    c = a + b
    if c < 0:
        raise NegativeSumError
    else:
        return c
