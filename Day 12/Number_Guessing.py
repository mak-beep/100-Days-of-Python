import random
import art

# System Variables
no_of_guess = 0
ended_ = False
EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def welcome():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def set_difficulty():
    choose = str(input("Choose a dificulty. Type 'easy' or 'hard' : "))
    global no_of_guess
    if choose == 'easy':
        no_of_guess = EASY_LEVEL_LIVES
    elif choose == 'hard':
        no_of_guess = HARD_LEVEL_LIVES

def check_answer(guess,number):
    if (guess is number):
        ended_ = True
        print("You guessed it Correctly.")
        return True
    else:
        if (guess > number):
            print("Too High.")
        elif (guess < number):
            print("Too Low.")
        return False

### Main Code ###

welcome()
selected_number = random.randint(1,100)
set_difficulty()

while (not ended_):
    guess = int(input("Make a Guess: "))
    ended_ = check_answer(guess,selected_number)
    if (ended_ == False):
        no_of_guess -= 1
        if (no_of_guess == 0):
            ended_ = True
            print("No more Tries Left.")
            print(f"The correct number was {selected_number}.")
