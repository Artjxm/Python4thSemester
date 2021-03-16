def f22(x):
    a = x & 0b111_111_111_111_11
    x >>= 14
    a <<= 0
    b = x & 0b1111_111
    x >>= 7
    b <<= 25
    c = x & 0b1111_1111_1
    x >>= 9
    c <<= 14
    d = x & 0b11
    d <<= 23
    return a + b + c + d


# print(hex(f22(0x272f25e7)))
# print(hex(f22(0xf15660af)))


