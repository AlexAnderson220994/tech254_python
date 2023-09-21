# Ask for a number

number = int(input("Choose any number you like: "))

# Multiples of 3 = Fizz
# Multiples of of 5 = Buzz
# Multiples of 3 and 5 = FizzBuzz

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)