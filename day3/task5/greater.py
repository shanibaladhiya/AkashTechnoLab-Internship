i = 0
while i < 3:
    num1 = int(input("Enter First number :\n"))
    num2 = int(input("Enter Second number :\n"))

    if num1 == num2:
        print(f"{num1} and {num2} is equal.")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num2} is greater than {num1}.")
    i += 1
    print("--------------------------------------")