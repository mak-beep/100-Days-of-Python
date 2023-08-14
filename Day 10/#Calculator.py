def calculator(num1):
    operation = input("+\n-\n*\n/\n")
    num2 = int(input("What's the next number? : "))
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    print(f"{num1} {operation} {num2} = {result}")
    return result

continue_choice = ""
result = 0
while True:
    if continue_choice != "y":
        num1 = int(input("Enter a number : "))
        result = num1  
    print(result)
    result = calculator(result)
    continue_choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation : ")
    
