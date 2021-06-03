class Cal6:
    def setdata(self, length):
        self.l = length

    def area(self):
        self.area = self.l ** 2

    def display(self):
        print(f"Area of square with length = {self.l} is {self.area}")


obj = Cal6()
length = int(input("enter length:\n"))
obj.setdata(length)
obj.area()
obj.display()
