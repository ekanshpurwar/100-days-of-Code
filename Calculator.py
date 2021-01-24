import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Addition
def add(n1,n2):
    return n1+n2

#Subtraction
def sub(n1,n2):
    return n1-n2

#Multiplication
def multiply(n1,n2):
    return n1*n2

#Division
def division(n1,n2):
    return n1/n2

def calculator():
    os.system("cls")
    print(logo)
    num1=float(input("Enter first number"))
    operator={"+":add,"-":sub,"*":multiply,"/":division}

    for symbol in operator:
        print(symbol)
    should_continue=True

    while should_continue:
        operation=input("Pick an operation from the line above")
        num2 = float(input("Enter next number"))
        calculation_function=operator[operation]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'y' to continue with the {answer}, or type 'n' to exit.")=='y':
            num1=answer
        else:
            should_continue=False
            calculator()

calculator()