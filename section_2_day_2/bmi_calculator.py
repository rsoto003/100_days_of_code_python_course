# 1kg = 2.20462 lb
# divide number of pounds by 2.20462 to get amount in kg
# 
# 1inch = 0.0254 meters
# multiply length in inches by 0.0254

weight = float(input("what is your weight in lbs?\n"))
weight = weight / 2.20462

height = float(input("what is your height in inches?\n"))
height = height * 0.0254

bmi = round(weight / height**2, 2)

print(f"Calculation complete. Your Body Mass Index (BMI) is: \n{bmi} %")
