class Sample:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum_int(self):
        return self.x + self.y

    def sub_int(self):
        return self.x-self.y

    def mul_int(self):
        return self.x*self.y

    def div_int(self):
        return self.x/self.y


if __name__ == "__main__":
    s = Sample(1, 2)
    print(s.sub_int())
    print(s.sum_int())
    print(s.mul_int())
    s.sub_int()
    s.sum_int()
    s.div_int()
    # print("\U+1F644")
    print("\U0001f600")
    print("\N{face with rolling eyes}")
