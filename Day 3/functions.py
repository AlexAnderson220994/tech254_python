"""
Functions

DRY (acronym) - Don't Repeat Yourself

- Allow us to embed/reference code, making it reusable.
"""

# Making a function

# def print_something(print_string): # clearly name arguments
#     print(print_string)
#
# print_something("We can pass anything in here!")
# print_something("Like this")

# def greeting(name):
#     print(f"Hello, my name is {name}")
#
# greeting("Alex")

# The return statement - holds a value

# def addition(int1, int2): # int1 and int2 are the arguments
#     return int1 + int2 # return is a function that needs to be added so the print knows to return something
#
# print(addition(2, 2))

def addition(int1=0, int2=0): # int1 and int2 are the arguments =adding numbers after makes those the defaults which can be overwritten.
    return int1 + int2 # return is a function that needs to be added so the print knows to return something

print(addition(5, 5))

# Multiple arguments

def multi_args(*multiargs): # star sounds for wildcard (as many as you want OR whatever you want it to be)
    for arg in multiargs:
        print(arg)
    print(type(multiargs))

multi_args(1, 2, 3, 4, 5, 6)

def holiday_days(days_worked):
    happy_days = days_worked * 21 / 365
    happy_days = round(happy_days)
    return happy_days


print(f"Wafa worked 250 days, so she can take {holiday_days(250)} day(s)")
print(f"Luke worked 12 days, so he can take {holiday_days(12)} day(s)")
print(f"Irina worked 79 days, so she can take {holiday_days(79)} day(s)")

# Type hints

# Functions good practices

# Add useful comments to explain your functions!
# Clear function names and argument names
# Keep your functions small and compact. Make them do one thing if possible.
# Avoid duplication.
# Correct indentation and formatting syntax
# Organised properly
# Do not use them unnecessarily
# Functions at the start of your code if possible
# Remember the return statement!
# Consider using type hints

