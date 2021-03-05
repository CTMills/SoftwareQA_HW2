#Caleb Mills
#Homework 2
import math

def retirement_option():
    age = int(input("\nPlease input your age in years: "))
    salary = int(input("\nPlease input your annual salary in dollars: "))
    savedPercent = int(input("\nPlease input percentage saved from salary: "))
    savingsGoal = int(input("\nPlease input your savings goal: "))

    if (age != int or salary != int or savedPercent != int or savingsGoal != int):
        print("You must enter whole numbers")
        error = -1
        return error

    if (age <= 0 or salary <= 0 or savedPercent <= 0 or savingsGoal <= 0):
        print("You must not enter 0 or lower")
        error = -1
        return error

    goalAge = retirement_calculate(age, salary, savedPercent, savingsGoal)
    if (goalAge >= 100):
        goalMet = False

    else:
        goalMet = True

    if (goalMet == True):
        phrase = "\nYou will meet your savings goal by " + str(goalAge) + " years old"

    else:
        phrase = "\nYou will not meet your savings goal"

    return phrase
    
def retirement_calculate (age, salary, savedPercent, savingsGoal):
    decimalPercent = savedPercent / 100
    savingsPerYear = round(salary * decimalPercent * 1.35, 5)
    yearsTilGoal = math.ceil(savingsGoal / savingsPerYear)
    goalAge = age + yearsTilGoal
    return goalAge
