#Caleb Mills
#Homework 2
#ctm364

from bmi import *
from retirement import *

def menu():
    while(1):
        print("\nMAIN MENU\nPress 1 to calculate your BMI and category\nPress 2 to calculate when you will reach your retirement goal\nPress 3 to exit the app")
        choice = int(input("\nEnter your choice: "))

        if (choice == 1):
            menu_output = bmi_option()
            print(menu_output)

        elif (choice == 2):
            menu_output = retirement_option()
            print(menu_output)

        elif (choice == 3):
            break

        else:
            print("\nThat is not a valid choice. Restarting interface...")

def main():
    menu()

main()
