import math


def f11(x, y, z):
    dec1 = (57 * pow(y, 4) + math.sin(z)) / \
           (21 * pow(y, 5) - 30 * z * z)
    sub = pow(z, 7) - 53 * pow(y, 8)
    dec2 = (pow(x, 4) - math.sin(z)) / \
           pow(y, 6) - pow(x, 7)
    result = dec1 - sub + dec2
    return '%.2e' % result


print(f11(15, 59, 39))
print(f11(-59, -54, 17))
