# BMI calculation
# weight (kg) / (height (m) * 2)
# convert height from cm to m by /100
# BMI = weight / (height/100)**2


user_height = 190
user_weight = 80

BMI = user_weight/(user_height/100)**2

print(f"BMI is {BMI}")



