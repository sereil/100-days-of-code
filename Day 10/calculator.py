import art
import os

logo = art.logo

print(logo)

def add(n1, n2):
    return n1+n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
"+":add,
"-":subtract,
"*":multiply,
"/":divide
}



    

def calculate():
    print(logo)
    first_num = float(input("What's the first number?: "))
    for operand in operations:
        print(operand)

    calc = True
    should_continue = True
    while should_continue == True: 
        operation_symbol = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))    
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_num, next_num)

        print(f"{first_num} {operation_symbol} {next_num} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start again.: ").lower() == "y":
            first_num = answer
        else:
            should_continue = False
            first_num = calculate()
            os.system("CLS") #Clear

calculate()