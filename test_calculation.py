# Testing functions for calculations

from bmi import *
from retirement import *

def test_bmi_calculate1():
    print("\nBMI Test Case 1:")
    out = bmi_calculate(70, 250)
    if(out == 36.7):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_bmi_calculate2():
    print("\nBMI Test Case 2:")
    out = bmi_calculate(50, 125)
    if(out == 36.0):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_bmi_calculate3():
    print("\nBMI Test Case 3:")
    out = bmi_calculate(70, 150)
    if(out == 22.0):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_bmi_calculate4():
    print("\nBMI Test Case 4:")
    out = bmi_calculate(70, 100)
    if(out == 14.7):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_bmi_calculate5():
    print("\nBMI Test Case 5:")
    out = bmi_calculate(70, 175)
    assert out == 25.7
    if(out == 25.7):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_retirement_calculate1():
    print("\nRetirement Test Case 1:")
    out = retirement_calculate(75, 255000, 15, 1000000)
    if(out == 95):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_retirement_calculate2():
    print("\nRetirement Test Case 2:")
    out = retirement_calculate(25, 450000, 5, 2500000)
    if(out == 108):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_retirement_calculate3():
    print("\nRetirement Test Case 3:")
    out = retirement_calculate(50, 50000, 5, 100000)
    if(out == 80):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_retirement_calculate4():
    print("\nRetirement Test Case 4:")
    out = retirement_calculate(45, 500000, 35, 10000000)
    if(out == 88):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def test_retirement_calculate5():
    print("\nRetirement Test Case 5:")
    out = retirement_calculate(50, 50000, 15, 1000000)
    if(out == 149):
        print("Test Passed: Expected Output = Actual Output")

    else:
        print("Test Failed")

def start_test():
    test_bmi_calculate1()
    test_bmi_calculate2()
    test_bmi_calculate3()
    test_bmi_calculate4()
    test_bmi_calculate5()
    test_retirement_calculate1()
    test_retirement_calculate2()
    test_retirement_calculate3()
    test_retirement_calculate4()
    test_retirement_calculate5()
start_test()