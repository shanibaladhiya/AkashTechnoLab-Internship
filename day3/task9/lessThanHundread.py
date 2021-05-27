number = int(input("Enter the number :\n"))
if number < 100:
    print(f"{number} is less than 100.")
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")
else:
    print("Enter number which is less than 100.")