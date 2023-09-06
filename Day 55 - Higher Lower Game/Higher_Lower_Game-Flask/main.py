from flask import Flask
from random import randint

number_to_guess = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home_page():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<number>")
def guess(number):
    number = int(number)
    if number == number_to_guess:
        return ('<h1 style="color: purple">You found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>')
    elif number > number_to_guess:
        return ('<h1 style="color: red">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>')
    elif number < number_to_guess:
        return ('<h1 style="color: green">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>')



if __name__ == "__main__":
    app.run(debug=True)
