import math


def f11(x, y, z):
    dec1 = (57 * y ** 4 + math.sin(z)) / \
           (21 * y ** 5 - 30 * z * z)
    sub = z ** 7 - 53 * y ** 8
    dec2 = (x ** 4 - math.sin(z)) / y ** 6 - x ** 7
    return dec1 - sub + dec2
