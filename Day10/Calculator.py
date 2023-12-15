from CalculatorArt import logo

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


print(logo)
go_again = True
num1 = float(input("What's the first number?: "))
for key in operations:
    print(key)
while go_again:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calculating = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 's' to start a new calculation : ")
    if continue_calculating == 'y':
        num1 = answer
    else:
        go_again = False
        print("Goodbye.")