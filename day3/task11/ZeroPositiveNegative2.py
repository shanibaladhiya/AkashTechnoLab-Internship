i = 0
while i < 3:
    number = int(input("Enter the number :\n"))
    if number >= 0:
        if number == 0:
            print(f"{number} is Zero")
        else:
            print(f"{number} is Positive")
    else:
        print(f"{number} is Negative")
    i += 1
    print("-------------------------------")