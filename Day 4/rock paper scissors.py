import random

results = ['rock','paper','scissor']

user_input = input("Rock, Paper, Scissors!!!!\n").lower()
computer_input = random.randint(0,2)
print(f"Computer chooses : {results[computer_input]}")
if user_input==results[computer_input]:
    print("Draw!")
else:
    if results[computer_input] == 'rock':
        if user_input == 'paper':
            print("You Won!")
        elif user_input == 'scissor':
            print("You Lost!")
    
    elif results[computer_input] == 'paper':
        if user_input == 'rock':
            print("You Lost!")
        elif user_input == 'scissor':
            print("You Won!")
    
    elif results[computer_input] == 'scissor':
        if user_input == 'paper':
            print("You Lost!")
        elif user_input == 'rock':
            print("You Won!")
    