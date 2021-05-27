number = int(input("Enter the number : \n"))
fact = 1
i = 1
while i <= number:
    fact = fact * i
    i += 1
print(f"Factorial of {number} is {fact}.")