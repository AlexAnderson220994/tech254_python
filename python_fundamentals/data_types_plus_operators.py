# What are operators?

# Symbols that execute a particular mathematical or logical function.

# Arithmetic operators:
# +, -, *, /, %.

# Logical (comparison) operators:
# >, <, == (equal to), != (not equal to), >=, <=.

# Numeric types
#int, float (floating point number - decimal), complex.

# comment out multiple lines using ctrl + /

# strings
single_quotes = 'Look! single quotes'
double_quotes = "Look! double quotes" # preferred option

# string slicing

# H e l l o   W o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11

hw = "Hello World!"

# print(hw[6:])
# print(hw[0:5])
# print(hw[-5:])

# string methods

strip_string = "Hi my name is Alex             "
# print(len(strip_string))
# print(len(strip_string.strip()))

example_text = "Here's some text with lots of text"

# print(example_text.count("text")) # .count counts the number of words or letters
# print(example_text.lower()) # turns characters into lower case

# Casting

# a = 1
# b = 2.5
# c = "3"
#
# print(a + b + int(c)) # int treats the "3" as an int and not a string
#
# # Concatenation
#
# d = " theres now a number 25.4 unless we put a space in"
#
# print(str(a) + ", " + str(b) + d)

# f-strings - formatted strings (no need for casting)

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")
#
# snoop = "Snoopy"
# snoop_years = 52
#
# print(f"{name.upper()} IS {snoop_years * 7} YEARS OLD IN DOG YEARS")

# Rounding

# pi = 3.14159265359
#
# print(f"Pi to 3 decimal places: {pi:.3f}")
# print(f"Pi to 5 decimal places: {pi:.5f}")

# Percentages

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}") # put the decimal place number between : and %
print(f"You scored {score/max_score:.0%}")