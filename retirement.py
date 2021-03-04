#Caleb Mills
#Homework 2
def retirement_calculate (age, salary, savedPercent, savingsGoal):
    savingsPerYear = salary * savedPercent * 1.35
    yearsTilGoal = savingsGoal / savingsPerYear
    goalAge = age + yearsTilGoal
    return goalAge
