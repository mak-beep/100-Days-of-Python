from flask import Flask

app = Flask(__name__)


# Advanced Decorators

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_italics(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


# To start the server from CLI
# flask --app hello run

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Different Routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_underline
@make_italics
def say_bye():
    return "<h1>Bye</h1>"


# Creating variable path and converting the path to a specified data type
# To store path into a variable, use this syntax '< variableName >'
@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hey there, {name}, you are {age} years old"




# To run it from the IDE
if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
