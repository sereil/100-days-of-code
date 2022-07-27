import art


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

calc = True

def calculate(n1):
    if n1 is None:        
        first_num = int(input("What's the first number?: "))
    else:
        print(f"Your first number is {n1}")
        first_num = n1

    second_num = int(input("What's the second number?: "))

    for operand in operations:
        print(operand)
    operation_symbol = input("Pick an operation from the line above: ")

    calculation_function = operations[operation_symbol]
    answer = calculation_function(first_num, second_num)

    print(f"{first_num} {operation_symbol} {second_num} = {answer}")
    keep_calculating = input(f"Type 'y' to continue with {answer}, or type 'n' to exit.: ").lower()

    if keep_calculating == 'y':
        calculate(answer)
    elif keep_calculating == 'n':
        print("Goodbye.")

calculate(n1=None)        
    
