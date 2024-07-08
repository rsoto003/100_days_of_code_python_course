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





if(bmi <= 18.5):
    print(f"Calculation complete. Your Body Mass Index (BMI) is: \n{bmi} %")
    print("\nYou are UNDERWEIGHT. Please consult your doctor on dietary changes necessary.")
elif(bmi >= 18.5 and bmi <= 24.9):
    print(f"Calculation complete. Your Body Mass Index (BMI) is: \n{bmi} %")
    print("\nYou are considered a HEALTH WEIGHT. NICE.")
elif(bmi >= 24.9 and bmi <= 29.9):
    print(f"Calculation complete. Your Body Mass Index (BMI) is: \n{bmi} %")
    print("\nYou are OVERWEIGHT. Please consult your doctor on dietary changes necessary.")
else:
    print(f"Calculation complete. Your Body Mass Index (BMI) is: \n{bmi} %")
    print("\nYou are considered to be OBESE. Please consult your doctor on dietary changes necessary.")