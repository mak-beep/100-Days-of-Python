def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }


num1 = int(input("What's the first number? "))
should_continue = True
while (should_continue):
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation shown in above line : ")
    function = operations[operation_symbol]
    num2 = int(input("What's the next number? "))
    result = function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    if input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation : ") == "y":
        num1 = result

    else:
        
        num1 = int(input("What's the first number? "))