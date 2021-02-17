def xor(a, b):
    if (bool(a) and bool(b)) or (not bool(a) and not bool(b)):
        return False
    elif bool(a):
        return a
    elif bool(b):
        return b
