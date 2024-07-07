#Calculator
from art import logo

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    b_should_continue = True

    while b_should_continue == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation ") == 'y':
            num1 = answer
        else:
            b_should_continue = False
            calculator()

calculator()


