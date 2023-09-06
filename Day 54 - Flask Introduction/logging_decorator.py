# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__} {args}")
        result = function(args[0], args[1])
        print(f"it returned {result}")

    return wrapper


# Use the decorator 👇

@logging_decorator
def addition(a, b):
    return a + b


addition(3, 5)
