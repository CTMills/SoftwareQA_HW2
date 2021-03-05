#Caleb Mills
#Homework 2
#ctm364

import math
from bmi import *
from retirement import *

def menu():
    while(1):
        try:
        print("\nMAIN MENU\nPress 1 to calculate your BMI and category\nPress 2 to calculate when you will reach your retirement goal\nPress 3 to exit the app")
        choice = int(input("\nEnter your choice: "))
            
        elif (choice == 1):
            menu_output = bmi_option()
            if (menu_output != -1):
                print(menu_output)

            else:
                print("You made an error. Restarting...")

        elif (choice == 2):
            menu_output = retirement_option()
            if (menu_output != -1):
                print(menu_output)

            else:
                print("You made an error. Restarting...")

        elif (choice == 3):
            break

        else:
            print("\nThat is not a valid choice. Restarting interface...")

    except:
        print("You made an error. Restarting...")

def main():
    menu()

main()
