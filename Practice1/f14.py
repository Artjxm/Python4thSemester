import math


def f14(n):
    if n == 0:
        return 5
    else:
        return math.tan(f14(n - 1)) + math.sin(f14(n - 1))


# print(f14(15))
# print(f14(3))
