print("------------------Operators--------------------")

x, y, z = 10, 20, 30
lst = [10, 20, 30, 40, 'hello', 'Shani']
print("------------------------------------------------")

print("<-----Arithmetic operators----->")
print(f"sum of {x} and {y} is  ", x + y)
print(f"Subtraction of {x} and {y} is  ", x - y)
print(f"Multiplication of {x} and {y} is ", x * y)
print(f"Division of {x} and {y} is" , x / y)
print(f"Floor Division of {x} and {y} is ", x // y)
print(f"Modulus of {x} and {y} is ", x % y)

print("<-----Comparison Operators----->")
print(f"{x}>{y}=", x > y)
print(f"{x}<{y}=", x < y)
print(f"{x}=={y}=", x == y)
print(f"{x}>={y}=", x >= y)
print(f"{x}<={y}=", x <= y)
print(f"{x}!={y}=", x != y)

print("<----Logical Operators---->")
print("-----and-----")
if x > y and x > z:
    print(f"{x} is the largest")
if y > x and y > z:
    print(f"{y} is the largest")
if (z > x and z > y):
    print(f"{z} is the largest")
print("----or----")
ch = input("enter char:")
if (
        ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
    print(f"{ch} is Vowel")
else:
    print(f"{ch} is not Vowel")

print("<----Membership Opearator---->")
print(f"{x} in lst:", x in lst)
print(f"{y} in lst:", y in lst)
print(f"{y} not in lst:", y not in lst)

print("<----Identity Opearator---->")
print(f"{x} is {y}:", x is y)
print(f"{x} is not {y}:", x is not y)

