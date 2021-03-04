#Caleb Mills
#Homework 2
import bmi
import retirement

def menu():
    while(1):
        print("\nMAIN MENU\nPress 1 to calculate your BMI and category\nPress 2 to calculate when you will reach your retirement goal\nPress 3 to exit the app")
        choice = int(input("\nEnter your choice: "))

        if (choice == 1):
            menu_output = bmi_option()

        elif (choice == 2):
            menu_output = retirement_option()

        elif (choice == 3):
            break

        else:
            print("\nThat is not a valid choice. Restarting interface...")

def main():
    menu()

main()
