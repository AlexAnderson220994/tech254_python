# BMI calculation
# weight (kg) / (height (m) * 2)
# convert height from cm to m by /100
# ** is square root
# BMI = weight / (height/100)**2


user_height = int(input("Height in cm: ")) # input user height here
user_weight = float(input("Weight in kg: ")) # input user weight here

BMI = user_weight/(user_height/100)**2

print("BMI is {BMI}")



