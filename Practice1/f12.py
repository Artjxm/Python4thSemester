import math


def f12(x):
    if x < 46:
        return 57 * x ** 4 + x / 21
    elif x < 139:
        return 73 * x ** 5 - math.cos(x)
    elif x < 184:
        return x ** 3 + x - math.sin(x)
    elif x < 246:
        return x ** 6 - x ** 7
    else:
        return 87 * x ** 3 - math.sin(x) - 73
