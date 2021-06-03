class Cal3:
    p = 0
    r = 0
    n = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calInterest(self):
        self.interest = (self.a * self.b * self.c) / 100
        print(f'Interest of {self.a} , {self.b} and {self.c} is {self.interest}')


obj = Cal3(40, 50, 55.5)
print("a = ", obj.a)
print("b = ", obj.b)
print("c = ", obj.c)
obj.calInterest()