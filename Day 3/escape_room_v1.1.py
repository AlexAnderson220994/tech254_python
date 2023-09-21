# Welcome to the escape room

# character variables
user_name_reg = input("Before we begin, tell me your name: ")


king_name = "King Aerys II"
host_name = "The King's Justice"

# location variables
location_one = "The Black Cells"
location_two = "The Red Keep"
location_three = "King's Landing"

# Name selector

name_prefix = ["Lord", "Lady", "Ser"]

# Create variable to choose character title
title_select = input(f"Please choose your desired title from {name_prefix}: ")

# Make a while loop incase wrong options are chosen (come back to this)

# Create variable to combine selected title with users name
user_name_mod = (f"{title_select} {user_name_reg}")


# Introduction to escape room
print(f"Good tidings, {user_name_mod}. I am {host_name}.")
print(f"Unfortunately you have ended up in {location_one} below {location_two} in {location_three} for treason.")
print(f"{king_name} intends to have you executed, however as {host_name} I know the secrets of the black cells to help you escape!")
print(f"To escape each section of {location_one}, you must answer a question. There are seven sections in total")


# Make a dictionary to define the questions
# Associate value to the key in the dictionary (question 1 = [0])
questions = [
    {
        "Question 1": "Where did House Targaryen originate?",
        "options": ["Volantis", "Astapor", "Valyria", "Braavos", "Meereen"],
        "correct_answer": "Valyria"
    },
    {
        "Question 2": "Who was the first Targaryen King?",
        "options": ["Jaeherys I", "Aegon I", "Baelor I", "Aerys I", "Maegor I"],
        "correct_answer": "Aegon I"
    },
    {
        "Question 3": "What was the name of the Castle in the Riverlands destroyed by Balerion the Black Dread?",
        "options": ["Winterfell", "Dreadfort", "Riverrun", "Castle Black", "Harrenhal"],
        "correct_answer": "Harrenhal"
    },
] # add more questions later


# Give a starting score of 0/7
score = 0 # variable to keep track of score

# Loop through the questions and ask them
# For loop
# enumerate is a function used to iterate through a sequence (needed for number options)
# question["options"] list of answer options and 1 is the value starting from
# Question 1
for question in questions: # iterates through each question in the dictionary 'questions' list
    print(question[list(question.keys())[0]])  # Print the questions. keys are assigned to each element of the dictionary and retrieved. [0] retrieves the first key which is the question text.
    for num, option in enumerate(question["options"], 1): # num and option are the two variables
        print(f"{num}. {option}")  # Print the options with numbers

    # Get the user's answer
    user_answer = input("Enter the number of your answer: ")

    # Check if the user's answer is correct
    if question["options"][int(user_answer) - 1] == question["correct_answer"]:
        print("Correct!\n") # \n is page break
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['correct_answer']}\n")

# Print the final score
print(f"Your final score is: {score}/{len(questions)}")

# Add if function to this sequence to go backwards to make it like an escape room
# Add a maximum number of attempts before it becomes game over

