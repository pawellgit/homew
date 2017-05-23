class round:
    s = 0

    def area(self, r):
        self.s = 3.14 * (r ** 2)

fig1 = round()
fig1.area(5)

print(fig1.s)

class rectangle:
    s = 0

    def area(self, a, b):
        self.s = a * b

fig2 = rectangle()
fig2.area(5, 6)

print(fig2.s)

