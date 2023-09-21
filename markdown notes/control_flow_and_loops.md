# Control Flow & Loops

## Control Flow

Control flow is the order in the code executes on Python. The control flow of a Python program is regulated by conditional statements and loops.

![control flow.JPG](..%2F..%2F..%2FPictures%2FDiagrams%2Fcontrol%20flow.JPG)

Check if conditions are true before you run a piece of code. Can think of each control flow statement as a boolean.

The control flow elements are **if, elif and else.**

See the below code for how to implement these conditional statements.

````
if film_rating.lower() == "u":
    print("All age groups can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance is advised")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People over 12 can watch this movie unsupervised. Younger people must be supervised")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie")
# else
else:
    print("This is not a valid rating, please use 'u', 'pg', '12', '12a', '15', '18'")
````

## For loops

A for loop is used for iterating over a sequence (list, tuple, dictionary, set, or string).
With the for loop, you can execute a set of statements for each item within a list, tuple or set. <br>


````
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Masha",
        "money": "£3.66"},
    3: {"name": "Roscoe",
        "money": "£1.14"}
````
````
for num in list_data:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print ("Gone too far!")
    else:
        print("Too soon!")
````

## While loops

With the while loop, you can execute a set of statements as long as the condition is true.

The while loop requires relevant variables to be ready. With the break statement, you can stop the loop even if the condition is true.

````
user_prompt = True

while user_prompt:
    age = input("What is your age?: ")
    if age.isdigit() and int(age) < 118:
        user_prompt = False
    else:
        print("Please provide your age in digits, below 118")

print(f"Your age is {age}")
````