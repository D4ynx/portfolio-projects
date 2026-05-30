def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

print(f"Your BMI is: {calculate_bmi(70, 1.75):.2f}")