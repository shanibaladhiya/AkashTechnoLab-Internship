year = int(input("Enter the year : \n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is Leap year.")
        else:
            print(f"{year} is not Leap year.")
    else:
        print(f"{year} is Leap year.")
else:
    print(f"{year} is not Leap year.")