num1 = int(input("Enter the First number :\n"))
num2 = int(input("Enter the Second number :\n"))
num3 = int(input("Enter the Third number :\n"))

if num1 >= num2:
    if num1 >= num3:
        print(f"{num1} is Greatest.")
    else:
        print(f"{num3} is Greatest.")
else:
    if num2 >= num3:
        print(f"{num2} is Greatest.")
    else:
        print(f"{num3} is Greatest.")
