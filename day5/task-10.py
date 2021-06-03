class Arith:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return f"Sum of {self.a} and {self.b} is {self.a+self.b}"

    def sub(self):
        return f"subtraction of {self.a} and {self.b} is {self.a - self.b}"

    def mul(self):
        return f"multiplication of {self.a} and {self.b} is {self.a * self.b}"

num1 = int(input("enter a: \n"))
num2 = int(input("enter b: \n"))

obj = Arith(num1, num2)
print(obj.sum())
print(obj.sub())
print(obj.mul())