class Cal1:
    def setdata(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        print(f"Sum of {self.a}, {self.b} and {self.c} is {self.a+self.b+self.c}")

nunbers = Cal1()
nunbers.setdata(5, 4, 8)
nunbers.display()