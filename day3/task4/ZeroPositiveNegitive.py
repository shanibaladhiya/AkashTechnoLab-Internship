i = 0
while i < 3: #for checking 3 differnt possibilities.
    number = int(input("Enter number :\n"))
    if number == 0:
        print(f"{number} is Zero")
    elif number > 0:
        print(f"{number} is Positive")
    else:
        print(f"{number} is Negative")
    i += 1
