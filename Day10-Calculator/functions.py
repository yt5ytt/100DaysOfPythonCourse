def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def dynamic_operation(n1, n2, operand):
    myFunction = operations[operand]
    result = myFunction(n1, n2)
    return result

def add(n1, n2):
    """Adding two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divide two numbers"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}