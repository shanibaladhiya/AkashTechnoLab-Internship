class Cal5:
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def calArea(self):
        self.area = self.l * self.w

    def display(self):
        print(f"Area of rectangle with length={self.l} and width ={self.w} is {self.area}")


length = int(input("enter length:\n"))
width = int(input("enter width:\n"))

obj = Cal5(length, width)
obj.calArea()
obj.display()