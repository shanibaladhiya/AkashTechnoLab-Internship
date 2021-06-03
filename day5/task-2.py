import math
class Cal2:
    def setdata(self, radius):
        self.r = radius

    def area(self):
        self.area_of_circle = math.pi*self.r*self.r

    def display(self):
        print(f"Area of the circle with radius={self.r} = {self.area_of_circle}")

area = Cal2()
area.setdata(5)
area.area()
area.display()
