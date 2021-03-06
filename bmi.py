#Caleb Mills
#Homework Assignment 2
def bmi_option():
    heightFeet = input("\nPlease insert your height in feet: ")
    heightInch = input("\nPlease insert your height in inches: ")
    weight = input("\nPlease insert your weight in pounds: ")

    if (heightFeet != int or heightInch != int or weight != int):
        print("Your weight and height must be a whole number")
        error = -1
        return error

    if (heightFeet <= 0 or heightInch <= 0 or weight <= 0):
        print("Your weight and height cannot be 0 or lower")
        error = -1
        return error
    
    height = (heightFeet * 12) + heightInch
    bmiAnswer = round(bmi_calculate(height, weight), 1)
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
    bmiFinal = round(metricWeight / bmiHeight, 1)
    return bmiFinal
