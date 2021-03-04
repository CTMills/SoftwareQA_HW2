#Caleb Mills
#Homework Assignment 2

def bmi_calculate (height, weight):
    metricWeight = weight * 0.45
    metricHeight = height * 0.025
    bmiHeight = metricHeight ** 2
    bmiFinal = metricWeight / bmiHeight
    return bmiFinal
