class C32:
    state = 'A'

    def bolt(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'H'
            return 6
        else:
            raise RuntimeError

    def daub(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise RuntimeError

    def cut(self):
        if self.state == 'C':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        elif self.state == 'G':
            self.state = 'B'
            return 11
        else:
            raise RuntimeError

    def scale(self):
        if self.state == 'F':
            self.state = 'H'
            return 9
        else:
            raise RuntimeError


# print("First case: ")
# a = C32()
# print(f"o.daub = {a.daub()}")
# print(f"o.cut = {a.cut()}")
# print(f"o.cut = {a.cut()}")
# print(f"o.cut = {a.cut()}")
# print(f"o.cut = {a.cut()}")
# print(f"o.daub = {a.daub()}")
# print(f"o.daub = {a.daub()}")
# print(f"o.daub = {a.daub()}")
# print(f"o.cut = {a.cut()}")
# # print(f"o.daub = {a.daub()}")
# print(f"o.scale = {a.scale()}")
#
#
# print("\nSecond case: ")
# b = C32()
# print(f"o.daub = {b.daub()}")
# print(f"o.daub = {b.daub()}")
# print(f"o.daub = {b.daub()}")
# print(f"o.cut = {b.cut()}")
# print(f"o.cut = {b.cut()}")
# print(f"o.cut = {b.cut()}")
# # print(f"o.cut = {b.cut()}")
# print(f"o.daub = {b.daub()}")
# print(f"o.cut = {b.cut()}")
# print(f"o.cut = {b.cut()}")
# print(f"o.cut = {b.cut()}")
# print(f"o.daub = {b.daub()}")
