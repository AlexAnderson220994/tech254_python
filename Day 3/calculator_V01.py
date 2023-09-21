# Function - addition

def add(x, y):
    return x + y

# Function - subtraction

def subtract(x, y):
    return x - y

# Function - multiplication

def multiply(x, y):
    return x * y

# Function - division

def divide(x, y):
    return x / y


# Use a While loop to display each option
while True:
    print("Choose Calculator function below:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
# user inputs below in the same loop
    user_input = input(": ")

    if user_input == "quit":
        break # use break to end function
    elif user_input in ("add", "subtract", "multiply", "divide"):# input linked to start of loop
        num1 = float(input("Enter first number: ")) # use float so number can be decimal
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))