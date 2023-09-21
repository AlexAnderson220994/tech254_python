# What is a Boolean?

# Binary option between True or False values.

a = True # has to be capitalised
b = False # has to be capitalised

# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True
# print(a <= b) # False
#
# # Logical/Comparison operators always give back true or false.
#
# print(2 > 1) # True

# print(True and False) # False
# print(True or False) # True

# Boolean methods

hi = "Hello world!"

# print(hi.isalpha()) # False
# print(hi.islower()) # False
# print(hi.endswith("!")) # True

# Boolean values

x = 0
y = 10

# print(bool(x)) # x = 0 and False = 0 so therefore x = False
# print(bool(y)) # if y is not equal to 0 it is true (doesn't have to be 1). Can also be negative.

# Value of None (null in other languages)
# Use as a placeholder value

z = None #independent of true and false

print(bool(z))
print(z == False)
print(z == None) # Not best practice
print(z is None) # best practice