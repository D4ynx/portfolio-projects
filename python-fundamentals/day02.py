def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category (bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
bmi = calculate_bmi(70, 1.75)
print(f"Your BMI is {bmi:.2f} - {bmi_category(bmi)}.")