## Function decorators
import time


def decorator_function(function):
    def wrapper_function():
        time.sleep(5)
        # add additional functionality
        function()

    return wrapper_function


# before defining a function, we can call the decorator to add additional functionality defined in the decorator,
# Doing this will make sure that functionality is embedded into the definition
@decorator_function
def say_hello():
    print("Hello")


# or we can add it for one instance
def say__bye():
    print("bye")


decorated_function = decorator_function(say__bye)
decorated_function()


## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("MAK")
new_user.is_logged_in = True
create_blog_post(new_user)
