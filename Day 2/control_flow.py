# Control Flow - Control the flow of your code (make decisions and ignore certain code dependent on factors)

# Check if conditions are true before you run a piece of code. Can think of each control flow statement as a boolean.

# if, elif, else

# if

# age = 18
#
# if age >= 18: # colon ends the condition
#     print("You are old enough to watch this movie")
# elif age < 18:
#     print("You are not old enough to watch this movie")
# elif - less processing power and runs only if the if condition is not met.

film_rating = "18"

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

# In python there are no switch statements or case statements.