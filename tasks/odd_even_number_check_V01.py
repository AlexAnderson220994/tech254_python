# User inputs number

number = int(input("Choose a number: "))

# Use modulo do determine if a number is a multiple of 2 and equal to 0
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

