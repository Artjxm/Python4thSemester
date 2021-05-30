# Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного
# умножения в столбик. Добавьте автоматическое тестирование,
# как в случае с naive_mul.

def naive_mul(x, y, res=0):
    for _ in range(y):
        res += x
    return res


def test_naive_mul():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("Works as intended :^)")


test_naive_mul()