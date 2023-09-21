# BMI calculation
# weight (kg) / (height (m) * 2)
# convert height from cm to m by /100
# ** is square root
# BMI = weight / (height/100)**2


#Input user height in cm
user_height = float(input("Enter your height in cm: "))

#Input user weight in kg
user_weight = float(input("Enter your weight in kg: "))

# Calculate BMI
BMI = user_weight / ((user_height / 100) ** 2)

print(f"Your BMI is: {BMI:.1f}")

# BMI result

if BMI < 18.5:
    result = "You are underweight"
elif 18.5 <= BMI < 24.9:
    result = "Your weight is Normal"
elif 25 <= BMI < 29.9:
    result = "You are overweight"
else:
    result = "You are obese"

print(f"Result: {result}")



