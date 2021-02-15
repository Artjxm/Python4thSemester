import math


def f12(x):
    if x < 46:
        result = 57 * pow(x, 4) + x / 21
        print('%.2e' % result)
    elif x < 139:
        result = 73 * pow(x, 5) - math.cos(x)
        print('%.2e' % result)
    elif x < 184:
        result = pow(x, 3) + x - math.sin(x)
        print('%.2e' % result)
    elif x < 246:
        result = pow(x, 6) - pow(x, 7)
        print('%.2e' % result)
    else:
        result = 87 * pow(x, 3) - math.sin(x) - 73
        print('%.2e' % result)

f12(141)
f12(16)