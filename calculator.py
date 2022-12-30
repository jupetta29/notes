import calculator_art


def add(n1, n2):
    '''Add'''
    return n1 + n2


def subtract(n1, n2):
    '''Subtract'''
    return n1 - n2


def multiply(n1, n2):
    '''Multiply'''
    return n1 * n2


def divide(n1, n2):
    '''Divide'''
    return n1 / n2


def convert_if_needed(number):
    if number % 1 == 0:
        return int(number)
    else:
        return number


operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide
}


def calculator():
    print(calculator_art.logo)

    num1 = float(input('What\'s the first number?\n'))

    print('\nAvailable Operations:')
    for symbol in operations:
        print(symbol)

    continue_calculations = True

    while continue_calculations:
        operation_symbol = input('\nPick an operation:\n')
        num2 = float(input('\nWhat\'s the next number?\n'))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        result = f'\nResult: {num1} {operation_symbol} {num2} = {answer}'

        print(result)

        should_continue = input(f'\nPress "y" to continue calculating with {answer}, \nPress "n" to start a new calculation, \nPress anything else to exit:\n').lower()

        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            continue_calculations = False
            calculator()
        else:
            print('\nGoodbye!')
            continue_calculations = False


calculator()