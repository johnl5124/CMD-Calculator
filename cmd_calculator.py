#!/usr/bin/python

class cmd_cal():
    counter = 0
    user_menu = print("""-------------CALCULATOR MENU-------------
    Addition = 1
    Subtraction = 2
    Multiply = 3 
    Division = 4 
    Exit = 5""")
    user_menu_input = input("Please enter a number (1-5): ")

    #addition
    def addition_function(x, y):
        return print("ANSWER: ", x, " + ", y, " = ", x + y)

    #subtraction
    def subtraction_function(x, y):
        return print("ANSWER: ", x, " - ", y, " = ", x - y)

    #multiplication
    def multiplication_function(x, y):
        return print("ANSWER: ", x, " x ", y, " = ", x * y)

    #division
    def division_function(x, y):
        return print("ANSWER: ", x, " / ", y, " = ", x // y)

    while counter == 0:
        if user_menu_input == str(1):
            print("-------------Addition-------------")
            x = int(input("Please enter a number: "))
            y = int(input("Please enter a number: "))
            addition_function(x, y)
        elif user_menu_input == str(2):
            print("-------------Subtraction-------------")
            x = int(input("Please enter a number: "))
            y = int(input("Please enter a number: "))
            subtraction_function(x, y)
        elif user_menu_input == str(3):
            print("-------------Multiplication-------------")
            x = int(input("Please enter a number: "))
            y = int(input("Please enter a number: "))
            multiplication_function(x, y)
        elif user_menu_input == str(4):
            print("-------------Division-------------")
            x = int(input("Please enter a number: "))
            y = int(input("Please enter a number: "))
            division_function(x, y)
        elif (user_menu_input < str(1) or user_menu_input > str(5)):
            print("ERROR! Please enter a number 1-5")
        elif user_menu_input == str(5):
            print("Thankyou! Exiting...")
            quit()
        user_menu = print("""-------------CALCULATOR MENU-------------
        Addition = 1
        Subtraction = 2
        Multiply = 3 
        Division = 4 
        Exit = 5""")
        user_menu_input = input("Please enter a number (1-5): ")
