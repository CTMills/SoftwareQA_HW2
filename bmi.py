#Caleb Mills
#Homework Assignment 2
def bmi_option():
    height = int(input("\nPlease insert your height in inches: "))
    weight = int(input("\nPlease insert your weight in pounds: "))
    bmiAnswer = bmi_calculate(height, weight)
    if (bmiAnswer < 18.5):
        bmiCategory = "Underweight"

    elif (bmiAnswer >= 18.5 and bmiAnswer <= 24.9):
        bmiCategory = "Normal"

    elif (bmiAnswer >= 25 and bmiAnswer <= 29.9):
        bmiCategory = "Overweight"

    else:
        bmiCategory = "Obese"

    bmiReport = "Your BMI is: " + str(bmiAnswer) + "\nYour BMI category is: " + bmiCategory
    return bmiReport

def bmi_calculate (height, weight):
    metricWeight = weight * 0.45
    metricHeight = height * 0.025
    bmiHeight = metricHeight ** 2
    bmiFinal = metricWeight / bmiHeight
    return bmiFinal
