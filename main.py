import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#print(operation["*"](4,8))
def calculator():
    print(art.logo)
    should_accumulate = True

    num1 = float(input('What is the first number?: '))

    while should_accumulate:

        for symbol in operation:
            print(symbol)

        # Check to make sure operation choice is valid
        operation_check = True
        while operation_check:
            operation_symbol = input("Pick an operation: ")
            if operation_symbol == '+' or operation_symbol == '-' or operation_symbol == '*' or operation_symbol == '/':
                operation_check = False
            else:
                print('Invalid operation! Pick again.')
                operation_check = True

        num2 = float(input("What is the next number?: "))
        answer = (operation[operation_symbol](num1, num2))
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print('\n' * 20)
            calculator()

calculator()