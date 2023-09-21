# While loops

# For loops are all to do with iterating through a collection

# While loops are more like a monitor -> while something is true then act.

x = 0

# while x < 10:
#     print(f"It's working --> {x}")
#     if x == 4:
#         break
#     x += 1
    # x += 1 # the += is an incrementer

# while loops can become infinite so be careful
# while loop used to execute a block of statements repeatedly until a given condition is satisfied.

user_prompt = True

while user_prompt:
    age = input("What is your age?: ")
    if age.isdigit() and int(age) < 118:
        user_prompt = False
    else:
        print("Please provide your age in digits, below 118")

print(f"Your age is {age}")