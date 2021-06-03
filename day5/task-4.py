class Cal4:
    def setdata(self, num):
        self.num = num

    def display(self):
        return self.num ** 2


number = Cal4()
num = int(input("enter any number:\n"))
number.setdata(num)
print(f"square of {num} is {number.display()}")