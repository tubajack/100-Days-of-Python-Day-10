#from replit import clear
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent,
    "%": modulo
}

def calculator():
    print(logo)
    should_add = True

    # Input the first number
    num1 = float(input("What is the first number?: "))

    while should_add:
        #Pick an operation
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")

        #Input the second number
        num2 = float(input("What is the second number?: "))

        #Print out the operations and the symbol
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        #Are we going to continue working with the result? Yes or No?
        choice = input(f"Type 'y' to continue calculating with {result} or 'n' to start over ")

        if choice == 'y':
            num1 = result
        else:
            should_add = False
            print("\n" * 20)
            calculator()

calculator()
