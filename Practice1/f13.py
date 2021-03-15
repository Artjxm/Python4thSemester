import math


def f13(n, m):
    sigma1 = sigma2 = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sigma1 += 57 * pow(i, 4) + math.sin(j)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sigma2 += 73 * pow(i, 5) - pow(i, 7)

    return sigma1 - sigma2
