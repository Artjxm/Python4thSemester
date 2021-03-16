import math


def f11(x, y, z):
    part1 = (57 * y ** 4 + math.sin(z)) / (21 * y ** 5 - 30 * z ** 2)

    part2 = z ** 7 - 53 * y ** 8

    part3 = (x ** 4 - math.sin(z)) / (y ** 6 - x ** 7)

    return part1 - part2 + part3


# print(f11(15, 59, 59))
# print(f11(-59, -54, 17))
