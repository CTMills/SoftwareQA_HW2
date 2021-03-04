#Caleb Mills
#Homework 2
def retirement_option():
    age = int(input("\nPlease input your age in years: "))
    salary = int(input("\nPlease input your annual salary in dollars: "))
    savedPercent = int(input("\nPlease input percentage saved from salary: "))
    savingsGoal = int(input("\nPlease input you savings goal: "))
    goalAge = retirement_calculate(age, salary, savedPercent, savingsGoal)
    if (goalAge >= 100):
        goalMet = false

    else:
        goalMet = true

    if (goalMet == true):
        phrase = "\nYou will meet your savings goal by" + str(goalAge) + "years old"

    else:
        phrase = "\nYou will not meet your savings goal"

    return phrase
    
def retirement_calculate (age, salary, savedPercent, savingsGoal):
    savingsPerYear = salary * savedPercent * 1.35
    yearsTilGoal = savingsGoal / savingsPerYear
    goalAge = age + yearsTilGoal
    return goalAge
